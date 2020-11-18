import pytest


@pytest.fixture
def post(user):
    from posts.models import Post
    return Post.objects.create(text='Тестовый пост 1', author=user)


@pytest.fixture
def group():
    from posts.models import Group
    return Group.objects.create(title='Тестовая группа 1', slug='test-link', description='Тестовое описание группы')


@pytest.fixture
def post_with_group(user, group):
    from posts.models import Post
    return Post.objects.create(text='Тестовый пост 2', author=user, group=group)
