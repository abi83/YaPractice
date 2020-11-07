from django.test import TestCase, Client
from django.urls import reverse

from posts.models import Post, Group, User


class ViewsTests(TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Making unauthorised client
        Creating 'First Group' and 'FirstUser'
        """
        super().setUpClass()
        cls.unauthorized_client = Client()
        cls.first_user = User.objects.create_user(
            username='FirstUser',
            first_name='First',
            last_name='Last',
        )
        cls.first_group = Group.objects.create(
            title='first_group',
            slug='first_slug',
            description='first_group description'
        )
        cls.first_post = Post.objects.create(
            text='First post',
            group=cls.first_group,
            author=cls.first_user,
        )

    def test_post_view_on_all_pages(self):
        """
        Creating new post with a group. Checking if post content is available
        at posts page, author profile page, simple post and group page
        """
        urls = [
            reverse('posts'),
            reverse('post', args=[self.first_post.author, self.first_post.pk]),
            reverse('group-posts', args=[self.first_group.slug]),
            reverse('profile', args=[self.first_user.username]),
        ]
        for url in urls:
            with self.subTest(url=url):
                response = self.unauthorized_client.get(url)
                self.assertTrue(
                    (self.first_post == response.context['post']) or
                    (self.first_post in response.context['posts']),
                    f'Page {url} dosnt contains post text')

    def test_groups_page(self):
        """
        Testing first_group appears on groups page
        """
        response = self.unauthorized_client.get(reverse('groups'))
        self.assertContains(response, self.first_group.title)
        self.assertContains(response, self.first_group.description)

    def test_authors_page(self):
        """
        Testing first_user appears on authors page
        """
        response = self.unauthorized_client.get(reverse('authors'))
        self.assertContains(response, self.first_user.first_name)
        self.assertContains(response, self.first_user.last_name)
