import sqlite3
from config import SQLITE_DB_TABLE
import logging


class SQLite:

    # Connect to db
    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
        logging.info("DB open connection")

    # Close connection to db
    def close(self):
        self.connection.close()
        logging.info("DB close connection")

    # Insert controller
    def insert_query(self, insert_query):
        self.cursor.execute(insert_query)
        self.connection.commit()
        self.cursor.close()
        self.close()

    # Update controller
    def update_query(self, update_query):
        self.cursor.execute(update_query)
        self.connection.commit()
        self.cursor.close()
        self.close()

    # Select controller, return list
    def select_query(self, select_query) -> list:
        rows = self.cursor.execute(select_query).fetchall()
        self.connection.commit()
        self.cursor.close()
        self.close()

        return rows
