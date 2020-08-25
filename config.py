import os

API_TOKEN = os.getenv("BOT_TOKEN")

# Settings for webhook
WEBHOOK_PATH = os.getenv("WEBHOOK_PATH")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

WEBAPP_HOST = os.getenv("WEBAPP_HOST")
WEBAPP_PORT = 5000

# Settings for SQLite
SQLITE_DB_NAME = "bot_db.db"
SQLITE_DB_TABLE = "users"