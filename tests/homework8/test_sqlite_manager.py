import os
import sqlite3

import pytest

from homework8.task2.task import TableData

os.chdir(f"{os.path.join(os.getcwd(), 'tests', 'homework8')}")


class TestSqliteManager:
    presidents = TableData(database_name="example.sqlite", table_name="presidents")

    def test_connect_db(self):
        assert self.presidents.cursor is not None

    def test_get_item_db(self):
        assert self.presidents["Yeltsin"] == ("Yeltsin", 999, "Russia")

    def test_get_count_rows(self):
        assert len(self.presidents) == 3

    def test_contains_item_positive(self):
        assert "Trump" in self.presidents

    def test_contains_item_negative(self):
        assert "President" not in self.presidents

    def test_iter_fields(self):
        presidents_lst = []
        for president in self.presidents:
            presidents_lst.append(president)
        assert len(presidents_lst) == 3

    def test_iter_fields_by_key(self):
        presidents_lst = []
        for president in self.presidents:
            presidents_lst.append(president["name"])
        assert presidents_lst == ["Yeltsin", "Trump", "Big Man Tyrone"]

    def test_close_db(self):
        self.presidents.__del__()
        with pytest.raises(sqlite3.ProgrammingError) as e:
            print(self.presidents["Yeltsin"])
        error_msg_cursor = e.value.args[0]
        assert error_msg_cursor == "Cannot operate on a closed database."
