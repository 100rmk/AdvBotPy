import logging
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from db.queries import select

from misc import dp, bot


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    db_user_id = select.get_user_by_id(message.from_user.id)

    logging.info(f"Command /start from user_id: {message.from_user.id}, user_name: {message.from_user.full_name}")

    if db_user_id == message.from_user.id:
        await bot.send_message(message.chat.id, "Вы авторизованны")
    else:
        markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(
            KeyboardButton('Отправить свой контакт ☎️', request_contact=True))

        await bot.send_message(message.chat.id,
                               "Вы не авторизрованы. Поделитесь своим номером для авторизации",
                               reply_markup=markup_request)
