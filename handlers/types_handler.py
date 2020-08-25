import logging
from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from db.queries import insert
from misc import dp, bot


# Handling the contact that the user sent
@dp.message_handler(content_types='contact')
async def contact_handler(message: types.Message):
    user_phone_number = str(message.contact.phone_number).replace("+", "")

    logging.info(f"""Func /handlers/types_handler.contact_handler add new contact user_id: {message.contact.user_id},
 first_name: {message.contact.first_name}, last_name: {message.contact.last_name}, phone_number: {user_phone_number}""")

    insert.insert_new_user(message.contact.user_id, message.contact.first_name,
                           message.contact.last_name, user_phone_number)

    await bot.send_message(message.chat.id, "Вы подписанны на обновления", reply_markup=ReplyKeyboardRemove())
