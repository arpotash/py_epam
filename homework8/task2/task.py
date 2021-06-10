import sqlite3
import sys
from collections import namedtuple


class TableData:
    def __init__(self, **kwargs):
        self.database = sqlite3.connect(kwargs["database_name"])
        self.table = kwargs["table_name"]
        self.cursor = self.database.cursor()
        self.query = self.cursor.execute(f"SELECT * from {self.table}")
        self.columns = [column[0] for column in self.cursor.description]

    def __del__(self):
        self.database.close()

    def __len__(self):
        self.query = self.cursor.execute(f"SELECT * from {self.table}")
        return len(self.cursor.fetchall())

    def __getitem__(self, item, data=None):
        for column in self.columns:
            self.cursor.execute(
                f"SELECT * from {self.table} WHERE {column}=:item", {"item": item}
            )
            data = self.cursor.fetchone()
            if data:
                return data

    def __contains__(self, item):
        self.query = self.cursor.execute(f"SELECT * from {self.table}")
        for row in self.query:
            if item in row:
                print(f"{item} in {self.table}")
                return True

    def __iter__(self):
        query = self.cursor.execute(f"SELECT * from {self.table}")
        name, *other = self.columns
        other_columns = " ".join(other)
        self.unique_value_column = [name[0] for name in query]
        self.column = namedtuple("Presidents_column", f"{name} {other_columns}")
        self.start = 0
        return self

    def __next__(self):
        if self.start >= len(
            self.cursor.execute(f"SELECT * FROM {self.table}").fetchall()
        ):
            raise StopIteration
        self.current_row = self.cursor.execute(
            f"SELECT * FROM {self.table} WHERE name=:value",
            {"value": self.unique_value_column[self.start]},
        ).fetchone()
        name, *other = self.current_row
        column = self.column(name, *other)._asdict()
        self.start += 1
        return column
