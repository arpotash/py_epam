from urllib.request import urlopen


def get_body(url):
    try:
        response = urlopen(url)
        if response.code == 200:
            data = response.read()
            html = data.decode("UTF-8")
            return html
    except:
        raise ValueError("url doesn't exist")


def count_dots_on_i(url: str) -> int:
    html = get_body(url)
    letter_count = html.count("i")
    return letter_count
