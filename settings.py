import os
from dotenv import load_dotenv, find_dotenv

# Loading .env variables
load_dotenv

TELEGRAM_TOKEN = "5685011290:AAE3zA-xypQUUbZZr0jtORszCHf2xrguhW8"
if TELEGRAM_TOKEN is None:
    raise Exception("Please setup the .env variable TELEGRAM_TOKEN.")

TELEGRAM_SUPPORT_CHAT_ID = "-1001458346880"
if TELEGRAM_SUPPORT_CHAT_ID is None or not str(TELEGRAM_SUPPORT_CHAT_ID).lstrip("-").isdigit():
    raise Exception("You need to specify 'TELEGRAM_SUPPORT_CHAT_ID' env variable: The bot will forward all messages "
                    "to this chat_id. Add this bot https://t.me/ShowJsonBot to your private chat to find its chat_id.")
TELEGRAM_SUPPORT_CHAT_ID = int(TELEGRAM_SUPPORT_CHAT_ID)


WELCOME_MESSAGE = os.getenv("WELCOME_MESSAGE", """Здравствуйте! Напишите ваш вопрос и мы ответим на него в течение 
рабочего дня  Если ваша организация является клиентом Академии Торговли для регистрации обращения напишите его по 
следующему шаблону: 1. Наименование вашей организации 2. Ваше Имя и контактный номер для связи 3. Текст вашего 
обращения 

После отправки сообщения с вами свяжется менеджер или специалист для решения вашего вопроса""")
REPLY_TO_THIS_MESSAGE = os.getenv("REPLY_TO_THIS_MESSAGE", "REPLY_TO_THIS")
WRONG_REPLY = os.getenv("WRONG_REPLY", "WRONG_REPLY")