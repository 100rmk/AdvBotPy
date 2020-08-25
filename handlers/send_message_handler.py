import logging
from misc import bot


async def advertising_sender(message, users_id):
    for user_id in users_id:
        logging.info(f"Func /handlers/send_message_handler.advertising_sender sending message to {user_id[0]},"
                     f" message: {message}")
        await bot.send_message(user_id[0], message)