import pytest
import random
import string


def random_string(string_length=15):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(string_length))


@pytest.fixture
def twilio_sid():
    return random_string()


class MockTwilioCreate:

    def __init__(self, to, from_=None, body=None, twilio_sid_val=None, **kwargs):
        assert to is not None, \
            'Проверьте, что вы указали куда отправить смс в функции `sms_sender` при отправке сообщения'
        assert from_ is not None, \
            'Проверьте, что вы указали куда c какого номера отправить смс в функции `sms_sender` при отправке сообщения'
        assert body is not None, \
            'Проверьте, что вы указали текст смс сообщения в функции `sms_sender` при отправке сообщения'
        self.sid = twilio_sid_val
        self.kwargs = kwargs


class MockTwilioMessages:

    def __init__(self, *args, twilio_sid_val=None, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.twilio_sid_val = twilio_sid_val

    def create(self, *args, **kwargs):
        return MockTwilioCreate(*args, twilio_sid_val=self.twilio_sid_val, **kwargs)


class MockTwilioClient:

    def __init__(self, *args, twilio_sid_val=None, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.twilio_sid_val = twilio_sid_val

    @property
    def messages(self):
        return MockTwilioMessages(twilio_sid_val=self.twilio_sid_val)


@pytest.fixture
def twilio_client(twilio_sid):

    return MockTwilioClient(twilio_sid_val=twilio_sid)

