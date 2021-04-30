from urllib.request import urlopen


def get_body(url):
    response = urlopen(url)
    if response.code == 200:
        data = response.read()
        html = data.decode("UTF-8")
        return html


def count_dots_on_i(url: str) -> int:
    html = get_body(url)
    letter_count = html.count("i")
    return letter_count
