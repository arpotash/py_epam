import asyncio
import json
from itertools import islice
from multiprocessing import Pool
from urllib import request
from xml.dom import minidom

import aiohttp
import requests
from bs4 import BeautifulSoup


def truncate(x, d):
    """
    Function rounds x to d digits

    :param x: float number
    :param d: int number of digits
    :return:  float number with d digits after decimal point
    """
    return int(x * (10.0 ** d)) / (10.0 ** d)


async def get_html(url, client, params=None):
    """
    Function returns web page html content

    :param url:
    :param client:
    :param params:

    :return: str, html page
    """
    async with client.get(url, params=params) as resp:
        return await resp.text()


def get_pages_count(html):
    """
    Function returns count of pagination pages
    on the website

    :param html: str, html content of the webpage
    :return: int, count of pagination pages
    """
    soup = BeautifulSoup(html, "lxml")
    pagination = soup.find("div", {"class": "finando_paging"}).find_all("a")
    if pagination:
        return int(next(reversed(pagination)).text)
    return 1


def get_list_pages(html, client):
    """
    Function returns organization details pages links list
    on a page

    :param html: str, html content of the webpage
    :return: list, links to the organization details page
    """
    links_content_lst = []
    soup = BeautifulSoup(html, "lxml")
    tds = soup.find_all("td", {"class": "table__td--big"})
    links = [td.find("a").get("href") for td in tds]
    return links


def get_organization_link(links, client):
    links_content_lst = []
    for link in links:
        organization_link = f"https://markets.businessinsider.com{link}"
        links_content_lst.append(get_html(organization_link, client))
    return links_content_lst


def create_xml_file_with_currency_data():
    """
    Function creates xml file with current value of main currencies

    :return: None
    """
    url = "http://www.cbr.ru/scripts/XML_daily.asp"
    web_file = request.urlopen(url)
    data = web_file.read()
    with open("currency.xml", "wb") as localFile:
        localFile.write(data)
    web_file.close()


def get_ruble_price():
    """
    Function parses current the USA dollar value and counts
    price in rubles

    :param dollar: float, price in dollars
    :return: float, price in rubles
    """
    create_xml_file_with_currency_data()
    doc = minidom.parse("currency.xml")
    dollar_elem = doc.getElementsByTagName("Valute")[10]
    currency = dollar_elem.getElementsByTagName("Value")[0].firstChild.data
    currency = currency.replace(",", ".")
    return float(currency)


def get_year_profit(soup_main, link):
    """
    Function finds year_profit in the organization

    :param soup_main: str, html content of the main webpage
    :param link, str, part of the link to the organization details page
    :return: str, organization's year_profit parameter
    """
    column_name = soup_main.find("tbody").find_all("td", {"class": "table__td--big"})
    for row in column_name:
        if row.find("a").get("href") == link:
            return row.find_parent("tr").find_all("td")[-1].text.split()[1]


def get_possible_profit(page_soup):
    """
    Function finds minimum and maximum prices and counts
    possible profit if the share would be bought at the minimum price
    and sold at the maximum price

    :param page_soup: str, html content of the detail organization page
    :return: float, organization's possible profit
    """
    min_price = float(
        page_soup.find("div", {"class": "snapshot__header"}, text="52 Week Low")
        .find_parent("div")
        .text.split()[0]
    )
    max_price = float(
        page_soup.find("div", {"class": "snapshot__header"}, text="52 Week High")
        .find_parent("div")
        .text.split()[0]
    )
    profit = min_price / 100
    return (max_price - min_price) / profit


def get_page_data(page):
    """
    Function parses main organization's parameters
    :param page: tuple of the (main page html content, link to the detail organization page,
    detail organization page html content, dollar rate in rubles according to Central Bank data)
    :return: dict, main organization's parameters
    """
    html, content_main, dollar_rate = page
    content, url = html
    try:
        data_dict = {}
        soup = BeautifulSoup(content, "lxml")
        soup_main = BeautifulSoup(content_main, "lxml")
        data_dict["name"] = soup.find(
            "span", {"class": "price-section__label"}
        ).text.rstrip()
        current_value_dollar = soup.find(
            "span", {"class": "price-section__current-value"}
        ).text
        data_dict["price"] = float(current_value_dollar) * dollar_rate
        data_dict[
            "code"
        ] = f'{soup.find("span", {"class": "price-section__category"}).find("span").text.strip()[2:]}'
        data_dict["pe"] = (
            soup.find("div", {"class": "snapshot__header"}, text="P/E Ratio")
            .find_parent("div")
            .text.split()[0]
            .replace(",", "")
        )
        data_dict["profit_year"] = get_year_profit(soup_main, url)
        data_dict["possible_profit"] = f"{truncate(get_possible_profit(soup), 4)}%"
        return data_dict
    except Exception:
        return


def write_to_json(data):
    """
    Function writes company data to json files

    :param data: list, company data
    :return: None
    """
    rich_companies = list(
        islice(sorted(data, key=lambda value: value["price"], reverse=True), 10)
    )
    companies_with_low_pe = list(
        islice(sorted(data, key=lambda value: float(value["pe"].replace(",", ""))), 10)
    )
    companies_with_high_growth_for_year = list(
        islice(
            sorted(
                data,
                key=lambda value: float(value["profit_year"].replace("%", "")),
                reverse=True,
            ),
            10,
        )
    )
    effective_companies = list(
        islice(
            sorted(
                data,
                key=lambda value: float(value["possible_profit"].replace("%", "")),
                reverse=True,
            ),
            10,
        )
    )
    with open("rich_companies.json", "w") as f_o:
        json.dump(rich_companies, f_o, indent=4)
    with open("companies_with_low_pe.json", "w") as f_o:
        json.dump(companies_with_low_pe, f_o, indent=4)
    with open("companies_with_high_growth_for_year.json", "w") as f_o:
        json.dump(companies_with_high_growth_for_year, f_o, indent=4)
    with open("effective_companies.json", "w") as f_o:
        json.dump(effective_companies, f_o, indent=4)


async def main():
    pages = []
    url = "https://markets.businessinsider.com/index/components/s&p_500"
    rubles = get_ruble_price()
    async with aiohttp.ClientSession() as client:
        html = await get_html(url, client)
        pages_count = get_pages_count(html)
        for page in range(1, pages_count + 1):
            html = await get_html(url, client, params={"p": page})
            data_by_page = get_list_pages(html, client)
            tasks = get_organization_link(data_by_page, client)
            responses = await asyncio.gather(*tasks)
            for resp in zip(responses, data_by_page):
                pages.append((resp, html, rubles))
    with Pool(processes=4) as pool:
        data = pool.map(get_page_data, pages)
        data = [row for row in data if row is not None]
    write_to_json(data)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
