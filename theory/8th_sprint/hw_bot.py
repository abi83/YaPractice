import time
import requests


PRACTICUM_TOKEN = 'AgAAAAAOr_1mAAYckTh1xNqfQkIjtODKyHHNcy8'


def get_homework_statuses():
    headers = {
        'Authorization': f'OAuth {PRACTICUM_TOKEN}',
    }
    r = requests.get('https://praktikum.yandex.ru/api/user_api/homework_statuses/', params={'from_date': 0}, headers=headers)
    return r.json()




