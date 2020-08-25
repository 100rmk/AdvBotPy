import logging

from aiohttp import web

from config import WEBHOOK_URL, WEBAPP_HOST, WEBAPP_PORT
from misc import dp, bot, app
import ssl
import handlers


async def on_startup(app):
    await bot.set_webhook(WEBHOOK_URL)
    logging.info("Bot start")


async def on_shutdown(app):
    logging.warning('Shutting down..')
    await bot.delete_webhook()


if __name__ == '__main__':
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)

    # Start web-application.
    web.run_app(app, host=WEBAPP_HOST, port=WEBAPP_PORT, ssl_context=ssl.CERT_NONE)
