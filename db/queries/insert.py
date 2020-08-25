import logging
from db.sqlite import SQLite
from config import SQLITE_DB_NAME, SQLITE_DB_TABLE


def insert_new_user(user_id, first_name, last_name, phone):
    query = f"""INSERT OR IGNORE INTO {SQLITE_DB_TABLE}
(user_id, first_name, second_name, phone)
VALUES ({user_id}, '{first_name}', '{last_name}', '{phone}');"""
    logging.info(f"Func /db/queries/insert.insert_new_user with {query}")
    SQLite(SQLITE_DB_NAME).insert_query(query)