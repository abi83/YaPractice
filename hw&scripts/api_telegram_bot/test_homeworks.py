from unittest import TestCase, mock

import requests_mock
from requests.exceptions import RequestException

from homework import get_homework_statuses, parse_homework_status

JSON = {'current_date': 1606672394,
        'homeworks': [
            {'date_updated': '2020-11-26T14:48:41Z',
             'homework_name': 'abi83__api_01_sms.zip',
             'id': 63318,
             'lesson_name': 'Отправка SMS-уведомлений',
             'reviewer_comment': 'Изучите рекомендации и попробуйте '
                                 'применить их в следующем ДЗ.',
             'status': 'approved'}, ]
        }


class TestReq(TestCase):

    @mock.patch('requests.get')
    def test_get_raised_request_exception(self, rq_get):
        msg = 'testing function'
        rq_get.side_effect = mock.Mock(side_effect=RequestException(msg))
        with self.assertRaises(RequestException) as e:
            get_homework_statuses(0)
            self.assertIn(msg, str(e.exception), msg='Wrong exception message')

    @mock.patch('requests.get')
    def test_get_raised_value_error(self, rq_get):
        jsons = [{'error': 'testing'}, {'code': 'testing'}]
        resp = mock.Mock()
        for json in jsons:
            with self.subTest(json=json):
                resp.json = mock.Mock(return_value=json)
                rq_get.return_value = resp
                self.assertRaises(ValueError, get_homework_statuses, 0)

    @requests_mock.Mocker()
    def test_get_raised_json_error(self, m):
        m.register_uri(
            'GET',
            'https://praktikum.yandex.ru/api/user_api/homework_statuses/',
            status_code=500)
        self.assertRaises(ValueError, get_homework_statuses, 0)

    @mock.patch('requests.get')
    def test_get_correct_return(self, rq_get):
        resp = mock.Mock()
        resp.json = mock.Mock(return_value=JSON)
        rq_get.return_value = resp
        self.assertEqual(get_homework_statuses(0), JSON)

    def test_parse_correct_return(self):
        call = parse_homework_status(JSON['homeworks'][0])
        self.assertIsInstance(call, str, 'Parse function returns not string')

    def test_parse_raises_key_error(self):
        wrong_dicts = [
            {'homework_name': 'test', },
            {'status': 'test', },
            {'test': 'test'},
        ]
        for hw in wrong_dicts:
            with self.subTest(homework=hw):
                self.assertRaises(KeyError, parse_homework_status, hw)
