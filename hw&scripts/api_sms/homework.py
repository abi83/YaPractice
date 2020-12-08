import os
import time

import requests
from dotenv import load_dotenv
from twilio.rest import Client


def get_status(user_id):
    access_token = os.getenv('VK_TOKEN')
    url = 'https://api.vk.com/method/users.get'
    params = {
        'user_ids': user_id,
        'fields': 'online',
        'v': 5.52,
        'access_token': access_token,
    }
    return requests.post(url, params=params).json()['response'][0]['online']


def sms_sender(sms_text):
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    twilio_number = os.getenv('NUMBER_FROM')
    my_number = os.getenv('NUMBER_TO')
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=sms_text,
        from_=twilio_number,
        to=my_number
    )
    return message.sid


if __name__ == '__main__':
    load_dotenv()

    vk_id = input('Введите id ')
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f'{vk_id} is online!')
            break
        time.sleep(5)
