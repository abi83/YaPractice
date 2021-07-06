from inspect import signature

import twilio.rest
import requests


class MockResponsePOST:

    def __init__(self, url, data=None, json=None, vk_sid=None, **kwargs):
        assert url == 'https://api.vk.com/method/users.get', \
            'Проверьте, что вы делаете запрос на правильный ресурс ВК для получения статуса пользователя'
        assert data is None, 'Проверьте, что вы не передаете никаких данных в тело запроса для ВК'
        assert 'params' in kwargs, 'Проверьте, что вы передали параметры `params` для запроса ВК'
        assert 'user_ids' in kwargs['params'], \
            'Проверьте, что в параметрах `params` для запроса ВК добавили id пользователя `user_ids`'
        assert 'fields' in kwargs['params'], \
            'Проверьте, что в параметрах `params` для запроса ВК добавили поле `fields`'
        assert kwargs['params']['fields'] == 'online', \
            'Проверьте, что в параметрах `params` для запроса ВК добавили поле `fields` со значением `online`'
        assert 'access_token' in kwargs['params'], \
            'Проверьте, что в параметрах `params` для запроса ВК добавили поле `access_token`'
        self.vk_sid = vk_sid

    def json(self):
        return {'response': [{'online': self.vk_sid}]}


class TestComment:

    def test_sms_sender(self, monkeypatch, twilio_client, twilio_sid):

        def mock_twilio_client(*args, **kwargs):
            return twilio_client

        monkeypatch.setattr(twilio.rest, "Client", mock_twilio_client)

        import homework

        assert hasattr(homework, 'sms_sender'), 'Функция `sms_sender()` не существует. Не удаляйте её.'
        assert hasattr(homework.sms_sender, '__call__'), 'Функция `sms_sender()` не существует. Не удаляйте её.'
        assert len(signature(homework.sms_sender).parameters) == 1, \
            'Функция `sms_sender()` должна быть с одним параметром.'

        result = homework.sms_sender('Test_message_check')
        assert result == twilio_sid, \
            'Проверьте, что возвращаете `sid` смс сообщения в результате работы функции `sms_sender`'

    def test_get_status(self, monkeypatch, vk_sid, response_get):

        def mock_response_get(*args, **kwargs):
            return response_get

        def mock_response_post(*args, **kwargs):
            return MockResponsePOST(*args, vk_sid=vk_sid, **kwargs)

        monkeypatch.setattr(twilio.rest, "Client", None)
        monkeypatch.setattr(requests, 'get', mock_response_get)
        monkeypatch.setattr(requests, 'post', mock_response_post)

        import homework

        assert hasattr(homework, 'get_status'), 'Функция `get_status()` не существует. Не удаляйте её.'
        assert hasattr(homework.get_status, '__call__'), 'Функция `get_status()` не существует. Не удаляйте её.'
        assert len(signature(homework.get_status).parameters) == 1, \
            'Функция `get_status()` должна быть с одним параметром.'

        result = homework.get_status(234435234)
        assert result == vk_sid, \
            'Проверьте, что возвращаете значение `online` в ответе API ВК в результате работы функции `get_status`'
