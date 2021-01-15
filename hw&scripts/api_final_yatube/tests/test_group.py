import pytest

from api.models import Group


class TestGroupAPI:

    @pytest.mark.django_db(transaction=True)
    def test_group_not_found(self, client, post, group_1):
        response = client.get('/api/v1/group/')

        assert response.status_code != 404, 'Страница `/api/v1/group/` не найдена, проверьте этот адрес в *urls.py*'

    @pytest.mark.django_db(transaction=True)
    def test_group_not_auth(self, client, post, group_1):
        response = client.get('/api/v1/group/')
        assert response.status_code == 200,\
            'Проверьте, что `/api/v1/group/` при запросе без токена возвращаете статус 200'

    @pytest.mark.django_db(transaction=True)
    def test_group_get(self, user_client, post, another_post, group_1, group_2):
        response = user_client.get('/api/v1/group/')
        assert response.status_code == 200, \
            'Проверьте, что при GET запросе `/api/v1/group/` с токеном авторизации возвращаетсся статус 200'

        test_data = response.json()

        assert type(test_data) == list, 'Проверьте, что при GET запросе на `/api/v1/group/` возвращается список'

        assert len(test_data) == Group.objects.count(), \
            'Проверьте, что при GET запросе на `/api/v1/group/` возвращается весь список групп'

        group = Group.objects.all()[0]
        test_group = test_data[0]
        assert 'id' in test_group, 'Проверьте, что добавили `id` в список полей `fields` сериализатора модели Group'
        assert 'title' in test_group, \
            'Проверьте, что добавили `title` в список полей `fields` сериализатора модели Group'

        assert test_group['id'] == group.id, \
            'Проверьте, что при GET запросе на `/api/v1/group/` возвращается весь список групп'

    @pytest.mark.django_db(transaction=True)
    def test_group_create(self, user_client, group_1, group_2):
        group_count = Group.objects.count()

        data = {}
        response = user_client.post('/api/v1/group/', data=data)
        assert response.status_code == 400, \
            'Проверьте, что при POST запросе на `/api/v1/group/` с не правильными данными возвращается статус 400'

        data = {'title': 'Группа  номер 3'}
        response = user_client.post('/api/v1/group/', data=data)
        assert response.status_code == 201, \
            'Проверьте, что при POST запросе на `/api/v1/group/` с правильными данными возвращается статус 201'

        test_data = response.json()

        msg_error = 'Проверьте, что при POST запросе на `/api/v1/group/` возвращается словарь с данными новой группы'
        assert type(test_data) == dict, msg_error
        assert test_data.get('title') == data['title'], msg_error

        assert group_count + 1 == Group.objects.count(), \
            'Проверьте, что при POST запросе на `/api/v1/group/` создается группа'

    @pytest.mark.django_db(transaction=True)
    def test_group_get_post(self, user_client, post, post_2, another_post, group_1, group_2):
        response = user_client.get('/api/v1/posts/')
        assert response.status_code == 200, \
            'Страница `/api/v1/posts/` не найдена, проверьте этот адрес в *urls.py*'
        test_data = response.json()
        assert len(test_data) == 3, \
            'Проверьте, что при GET запросе на `/api/v1/posts/` возвращается список всех постов'

        response = user_client.get(f'/api/v1/posts/?group={group_2.id}')
        assert len(response.json()) == 1, \
            'Проверьте, что при GET запросе с параметром `group` на `/api/v1/posts/` ' \
            'возвращается список соответствующих постов'

        response = user_client.get(f'/api/v1/posts/?group={group_1.id}')
        assert len(response.json()) == 2, \
            'Проверьте, что при GET запросе с параметром `group` на `/api/v1/posts/` ' \
            'возвращается список соответствующих постов'
