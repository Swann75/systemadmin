import sqlite3
import pandas


class Database:
    def __init__(self, database: str, table: str) -> None:
        """
        Initialize the object
        :param database: str
        :param table: str
        """
        self.database = database
        self.table = table
        self.connection = sqlite3.connect(database)

    def select(self, table: str) -> None:
        self.connection.execute(f"select * from {table}")

    def insert(self, dictionary: dict) -> None:
        if type(dictionary) is dict:
            pass

