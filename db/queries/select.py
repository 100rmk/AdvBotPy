import logging
from db.sqlite import SQLite
from config import SQLITE_DB_NAME, SQLITE_DB_TABLE


def get_user_by_id(user_id) -> int:
    query = f"SELECT user_id FROM {SQLITE_DB_TABLE} WHERE user_id = {user_id};"
    logging.info(f"Func /db/queries/select.get_user_by_id with {query}")
    response = SQLite(SQLITE_DB_NAME).select_query(query)
    if len(response) > 0:
        return response[0][0]


def get_users_by_phone_number(phones_number) -> list:
    query = f"SELECT user_id FROM {SQLITE_DB_TABLE} WHERE "
    for i in range(len(phones_number)):
        query += f"phone = '{phones_number[i]}' OR "
        if i == len(phones_number) - 1:
            query += f"phone = '{phones_number[i]}'"
    logging.info(f"Func /db/queries/select.get_users_by_phone_number with {query}")
    response = SQLite(SQLITE_DB_NAME).select_query(query)
    return response
