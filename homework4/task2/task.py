from unittest.mock import patch
from urllib.request import urlopen


def count_dots_on_i(url: str) -> int:
    response = urlopen(url)
    count = 0
    if response.code == 200:
        data = response.read()
        html = data.decode("UTF-8")
        for line in html:
            if line in ["i", "I"]:
                count += 1
    else:
        raise ValueError("Url doesn't exist")
    return count
