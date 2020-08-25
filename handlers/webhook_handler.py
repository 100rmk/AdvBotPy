import logging

from aiohttp import web
from misc import app
import json
from db.queries import select
from handlers import send_message_handler
from Exceptions import PassVerificationException

routes = web.RouteTableDef()


# Receiving advertising messages by post request and sending to users
@routes.post("/webhook/advertising_message")
async def advertising_mailing_handler(request: web.Request):
    try:
        json_data = await request.json()
        app_id = json_data["app_id"]
        message = json_data["message"]
        phones = json_data["phones"]

        logging.info("POST request advertising_mailing_handler with json", json_data)

        # pseudo authentication
        if int(app_id) != 1:
            raise PassVerificationException()

        if request.body_exists and len(phones) > 0:
            # Call db and receive all ids by phone numbers from the request
            users_id = select.get_users_by_phone_number(phones)
            # Calling the function for sending messages
            await send_message_handler.advertising_sender(message, users_id)

            return web.json_response(text=json.dumps({
                'status': 'success'
            }), status=200)

    except PassVerificationException:
        return web.json_response(text=json.dumps({
            "error": 401,
            "message": "Wrong authentication key"
        }), status=401)

    except Exception as e:
        response_obj = {
            'status': 'failed',
            'reason': str(e)
        }
        return web.json_response(text=json.dumps(response_obj), status=500)

app.add_routes(routes)
