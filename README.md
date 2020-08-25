# Advertising sender bot
![](img/tg_icon.png)
#### Description
Telegram bot for sending messages to users through post requests

#### What it bot for?
This bot is needed for companies that want to send new messages to their users via telegram

## Quick start
1. Clone project
> git@github.com:hinesqui/GatewayBotPy.git

2. Open project path
> cd ./GatewayBotPy

3. Install requirements 
> pip3 install -r ./requirements.txt

4. Set variables in config.py
> You can write variables directly in the code, but it is recommended to set variables through [ENV](https://en.wikipedia.org/wiki/Environment_variable)

- For macOS and Linux Distributions
> export BOT_TOKEN=1234567890:ABCDEFqwerty_asdf

> export WEBHOOK_PATH=127.0.0.1

- For windows

> run cmd -> sysdm.cpl -> Advanced -> Environment Variables -> System(or User) Variables -> New

5. Create db in project path then create table "users" via SQLite 
> Use createdb.sql

6. Run bot.py

For test post request use curl
    
        curl --location --request POST 'https://da03c17ed9b3.ngrok.io/webhook/advertising_message' \
    --header 'Content-Type: text/plain' \
    --data-raw '{
        "app_id": 1,
        "message": "Your message",
        "phones": [
            "79161234567",
            "79171234567"
        ]
    }'
    
JSON look like 
    
    {
        "app_id": 1,
        "message": "Test message",
        "phones": [
            "79161234567"
        ]
    }
    
## Example
![](img/example.gif)
