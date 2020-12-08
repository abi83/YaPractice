import logging
import os
import time

import requests
import telegram
from dotenv import load_dotenv
from requests.exceptions import RequestException

load_dotenv()
PRAKTIKUM_TOKEN = os.getenv('PRAKTIKUM_TOKEN')
PRAKTIKUM_URL = 'https://praktikum.yandex.ru/api/user_api/homework_statuses/'
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

HW_VERDICT = {
    'approved': 'Ревьюеру всё понравилось, можно приступать '
                'к следующему уроку.',
    'rejected': 'К сожалению в работе нашлись ошибки.', }
MSG_TEMPLATE = 'У вас проверили работу "{hw_name}"!\n\n{verdict}'
JSON_CHANGED_MSG = 'Homework has unknown status "{hw_status}". ' \
                   'Expected one from {statuses}'
CONNECTION_ERR_MSG = 'Connection problem: {error}, {request_params}'
OUTPUT_ERR_MSG = 'Remote server error message: {}'
OUTPUT_CODE_MSG = 'Remote server code message: {}'
REQUEST_DATA = 'Request params: {}'


def parse_homework_status(homework: dict) -> str:
    """
    gets necessary data from yandex API response or raises
    Exception if response format is unknown
    :param homework: response data
    :return: message to be sent
    :raises: ValueError if desired value was not found
    """
    hw_name = homework['homework_name']
    hw_status = homework['status']
    if hw_status not in HW_VERDICT:
        raise ValueError(JSON_CHANGED_MSG.format(
            hw_status=hw_status,
            statuses=HW_VERDICT)
        )
    logging.debug('Homework status successfully parsed')
    return MSG_TEMPLATE.format(hw_name=hw_name, verdict=HW_VERDICT[hw_status])


def get_homework_statuses(current_timestamp: int) -> dict:
    """
    Makes yandex praktikum API request, to find homeworks data from
    current_timestamp moment
    :param current_timestamp: from_date in Unix seconds, to request all
    homeworks after it
    :return: response in dict format
    :raises: Exception if occurred
    """
    request_params = {
        'url': PRAKTIKUM_URL,
        'headers': {'Authorization': f'OAuth {PRAKTIKUM_TOKEN}', },
        'params': {'from_date': current_timestamp},
    }
    try:
        response = requests.get(**request_params)
    except RequestException as error:
        raise RequestException(CONNECTION_ERR_MSG.format(
            error=error, request_params=request_params)) from error
    output = response.json()
    logging.debug(f'Praktikum response received {output}')
    if output.get('error'):
        raise ValueError(OUTPUT_ERR_MSG.format(output['error']),
                         REQUEST_DATA.format(request_params))
    if output.get('code'):
        raise ValueError(OUTPUT_CODE_MSG.format(output['code']),
                         REQUEST_DATA.format(request_params))
    return output


def send_message(message: str, bot_client=None):
    if not bot_client:
        bot_client = telegram.Bot(token=TELEGRAM_TOKEN)
    return bot_client.send_message(chat_id=CHAT_ID, text=message)


def main():
    pause = 10 * 60
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    current_timestamp = int(time.time())
    errors = 0
    while True:
        try:
            new_homework = get_homework_statuses(current_timestamp)
            if new_homework.get('homeworks'):
                send_message(
                    parse_homework_status(
                        new_homework.get('homeworks')[0]), bot)
                logging.info('Message seems to be sent')
            current_timestamp = new_homework.get('current_date',
                                                 current_timestamp)
            errors = 0
            time.sleep(pause)
        except Exception as e:
            logging.exception(f'{e}')
            errors += 1
            time.sleep(pause)
        else:
            logging.debug('Checked without exceptions')
        finally:
            if errors > 10:
                send_message('More than 10 errors happened', bot)
                logging.error('More than 10 errors happened')
                errors = 0
                time.sleep(pause*2)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        filename=__file__ + '.log',
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S')
    main()
