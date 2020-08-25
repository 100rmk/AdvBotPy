import logging

from aiogram.dispatcher.webhook import get_new_configured_app

from config import API_TOKEN, WEBHOOK_PATH
from aiogram import Bot, Dispatcher

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
app = get_new_configured_app(dispatcher=dp, path=WEBHOOK_PATH)

logging.basicConfig(level=logging.INFO)

