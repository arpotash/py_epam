from unittest.mock import Mock
from urllib.error import URLError

import pytest

from homework4.task2.task import count_dots_on_i


class TestCountDotsOnUrl:
    def test_find_count_letter(self, monkeypatch):
        urlopen_mock = Mock()
        urlopen_mock.read.decode = Mock(return_value="iiieee")
        monkeypatch.setattr("homework4.task2.task.get_body", urlopen_mock.read.decode)
        assert count_dots_on_i("xxxx") == 3

    def test_is_exist_url(self):
        with pytest.raises(URLError) as e:
            count_dots_on_i("http://wewwwewe.com/")
