import pytest
import random
import string


def random_string(string_length=15):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(string_length))


@pytest.fixture
def vk_sid():
    return random_string()


class MockResponseGET:
    @staticmethod
    def json():
        assert False, 'Проверьте, что используете метод POST для ВК'


@pytest.fixture
def response_get():
    return MockResponseGET()
