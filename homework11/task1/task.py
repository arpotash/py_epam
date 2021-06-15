import asyncio
import json
from itertools import islice
from multiprocessing import Pool
from urllib import request
from xml.dom import minidom

import aiohttp
from bs4 import BeautifulSoup


def truncate(x, d):
    return int(x * (10.0 ** d)) / (10.0 ** d)


async def get_html(url, client, params=None):
    async with client.get(url, params=params) as resp:
        return await resp.text()


def get_pages_count(html):
    soup = BeautifulSoup(html, "lxml")
    pagination = soup.find("div", {"class": "finando_paging"}).find_all("a")
    if pagination:
        return int(next(reversed(pagination)).text)
    return 1


def get_list_pages(html):
    soup = BeautifulSoup(html, "lxml")
    tds = soup.find_all("td", {"class": "table__td--big"})
    links = [td.find("a").get("href") for td in tds]
    return links


def get_organization_page(links, client):
    links_content_lst = []
    for link in links:
        organization_link = f"https://markets.businessinsider.com{link}"
        links_content_lst.append(get_html(organization_link, client))
    return links_content_lst


def get_organization_link(links):
    links_content_lst = []
    for link in links:
        organization_link = f"https://markets.businessinsider.com{link}"
        links_content_lst.append(organization_link)
    return links_content_lst


def create_xml_file_with_currency_data():
    url = "http://www.cbr.ru/scripts/XML_daily.asp"
    web_file = request.urlopen(url)
    data = web_file.read()
    with open("currency.xml", "wb") as localFile:
        localFile.write(data)
    web_file.close()


def get_ruble_price(dollar):
    create_xml_file_with_currency_data()
    doc = minidom.parse("currency.xml")
    dollar_elem = doc.getElementsByTagName("Valute")[10]
    currency = dollar_elem.getElementsByTagName("Value")[0].firstChild.data
    currency = currency.replace(",", ".")
    return float(currency) * float(dollar)


def get_year_profit(soup_main, html):
    column_name = soup_main.find("tbody").find_all("td", {"class": "table__td--big"})
    for row in column_name:
        if row.find("a").get("href") == html:
            return row.find_parent("tr").find_all("td")[-1].text.split()[1]


def get_possible_profit(page_soup):
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


def get_page_data(content, content_main, link):
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
        data_dict["price"] = get_ruble_price(current_value_dollar)
        data_dict[
            "code"
        ] = f'{soup.find("span", {"class": "price-section__category"}).find("span").text.strip()[2:]}'
        data_dict["pe"] = (
            soup.find("div", {"class": "snapshot__header"}, text="P/E Ratio")
            .find_parent("div")
            .text.split()[0]
            .replace(",", "")
        )
        data_dict["profit_year"] = get_year_profit(soup_main, link)
        data_dict["possible_profit"] = f"{truncate(get_possible_profit(soup), 4)}%"
        return data_dict
    except Exception:
        return


def write_to_json(data):
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
    async with aiohttp.ClientSession() as client:
        html = await get_html(url, client)
        pages_count = get_pages_count(html)
        for page in range(1, pages_count + 1):
            html = await get_html(url, client, params={"p": page})
            data_by_page = get_list_pages(html)
            tasks = get_organization_page(data_by_page, client)
            responses = await asyncio.gather(*tasks)
            for resp in zip(responses, data_by_page):
                pages.append((resp, html))
    data_lst = list()
    with Pool(processes=4) as pool:
        for page in pages:
            html, content_main = page
            content, url = html
            data = pool.apply(get_page_data, args=(content, content_main, url))
            if data:
                data_lst.append(data)
    write_to_json(data_lst)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
