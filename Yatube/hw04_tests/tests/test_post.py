import pytest

from django.core.paginator import Paginator, Page
from django.contrib.auth import get_user_model
from django import forms

from posts.models import Post


def get_field_context(context, field_type):
    for field in context.keys():
        if field not in ('user', 'request') and type(context[field]) == field_type:
            return context[field]
    return


class TestPostView:

    @pytest.mark.django_db(transaction=True)
    def test_post_view_get(self, client, post_with_group):
        try:
            response = client.get(f'/{post_with_group.author.username}/{post_with_group.id}')
        except Exception as e:
            assert False, f'''Страница `/<username>/<post_id>/` работает неправильно. Ошибка: `{e}`'''
        if response.status_code in (301, 302):
            response = client.get(f'/{post_with_group.author.username}/{post_with_group.id}/')
        assert response.status_code != 404, \
            'Страница `/<username>/<post_id>/` не найдена, проверьте этот адрес в *urls.py*'

        profile_context = get_field_context(response.context, get_user_model())
        assert profile_context is not None, \
            'Проверьте, что передали автора в контекст страницы `/<username>/<post_id>/`'

        post_context = get_field_context(response.context, Post)
        assert post_context is not None, \
            'Проверьте, что передали статью в контекст страницы `/<username>/<post_id>/` типа `Post`'


class TestPostEditView:

    @pytest.mark.django_db(transaction=True)
    def test_post_edit_view_get(self, client, post_with_group):
        try:
            response = client.get(f'/{post_with_group.author.username}/{post_with_group.id}/edit')
        except Exception as e:
            assert False, f'''Страница `/<username>/<post_id>/edit/` работает неправильно. Ошибка: `{e}`'''
        if response.status_code in (301, 302) and not response.url.startswith(f'/{post_with_group.author.username}/{post_with_group.id}'):
            response = client.get(f'/{post_with_group.author.username}/{post_with_group.id}/edit/')
        assert response.status_code != 404, \
            'Страница `/<username>/<post_id>/edit/` не найдена, проверьте этот адрес в *urls.py*'

        assert response.status_code in (301, 302), \
            'Проверьте, что вы переадресуете пользователя со страницы `/<username>/<post_id>/edit/` на страницу поста, если он не автор'

    @pytest.mark.django_db(transaction=True)
    def test_post_edit_view_author_get(self, user_client, post_with_group):
        try:
            response = user_client.get(f'/{post_with_group.author.username}/{post_with_group.id}/edit')
        except Exception as e:
            assert False, f'''Страница `/<username>/<post_id>/edit/` работает неправильно. Ошибка: `{e}`'''
        if response.status_code in (301, 302):
            response = user_client.get(f'/{post_with_group.author.username}/{post_with_group.id}/edit/')
        assert response.status_code != 404, \
            'Страница `/<username>/<post_id>/edit/` не найдена, проверьте этот адрес в *urls.py*'

        post_context = get_field_context(response.context, Post)
        assert post_context is not None, \
            'Проверьте, что передали статью в контекст страницы `/<username>/<post_id>/edit/` типа `Post`'

        assert 'form' in response.context, \
            'Проверьте, что передали форму `form` в контекст страницы `/<username>/<post_id>/edit/`'
        assert len(response.context['form'].fields) == 2, \
            'Проверьте, что в форме `form` на страницу `/<username>/<post_id>/edit/` 2 поля'
        assert 'group' in response.context['form'].fields, \
            'Проверьте, что в форме `form` на странице `/new/` есть поле `group`'
        assert type(response.context['form'].fields['group']) == forms.models.ModelChoiceField, \
            'Проверьте, что в форме `form` на странице `/new/` поле `group` типа `ModelChoiceField`'
        assert not response.context['form'].fields['group'].required, \
            'Проверьте, что в форме `form` на странице `/new/` поле `group` не обязательно'

        assert 'text' in response.context['form'].fields, \
            'Проверьте, что в форме `form` на странице `/new/` есть поле `text`'
        assert type(response.context['form'].fields['text']) == forms.fields.CharField, \
            'Проверьте, что в форме `form` на странице `/new/` поле `text` типа `CharField`'
        assert response.context['form'].fields['text'].required, \
            'Проверьте, что в форме `form` на странице `/new/` поле `group` обязательно'

    @pytest.mark.django_db(transaction=True)
    def test_post_edit_view_author_post(self, user_client, post_with_group):
        text = 'Проверка изменения поста!'
        try:
            response = user_client.get(f'/{post_with_group.author.username}/{post_with_group.id}/edit')
        except Exception as e:
            assert False, f'''Страница `/<username>/<post_id>/edit/` работает неправильно. Ошибка: `{e}`'''
        url = f'/{post_with_group.author.username}/{post_with_group.id}/edit/' if response.status_code in (301, 302) else f'/{post_with_group.author.username}/{post_with_group.id}/edit'

        response = user_client.post(url, data={'text': text, 'group': post_with_group.group_id})

        assert response.status_code in (301, 302), \
            'Проверьте, что со страницы `/<username>/<post_id>/edit/` после создания поста перенаправляете на страницу поста'
        post = Post.objects.filter(author=post_with_group.author, text=text, group=post_with_group.group).first()
        assert post is not None, \
            'Проверьте, что вы изминили пост при отправки формы на странице `/<username>/<post_id>/edit/`'
        assert response.url.startswith(f'/{post_with_group.author.username}/{post_with_group.id}'),\
            'Проверьте, что перенаправляете на страницу поста `/<username>/<post_id>/`'
