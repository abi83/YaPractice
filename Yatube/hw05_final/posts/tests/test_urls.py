from uuid import uuid1
from random import randint

from django.test import TestCase, Client
from django.urls import reverse

from posts.models import Post


class URLTests(TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Making unauthorised client
        """
        super().setUpClass()
        cls.unauthorized_client = Client()

    def test_homepage(self):
        """
        Checking 200 answer directly at '/'
        """
        response = self.unauthorized_client.get('')
        self.assertEqual(response.status_code, 200)

    def test_unauthorized_user_new_post(self):
        """
        Test of redirecting unauthorised user from '/new/' page
        with get and post methods
        """
        target_url = reverse('login') + '?next=' + reverse('new-post')
        post_count = Post.objects.count()
        posts_before_test = list(Post.objects.order_by('pk').all())
        responses = {
            'get': self.unauthorized_client.get(
                reverse('new-post'), follow=False),
            'post': self.unauthorized_client.post(
                reverse('new-post'),
                {'text': 'Test unauthorized user new post'}, follow=False)}
        for response in responses.values():
            with self.subTest(response=response):
                self.assertRedirects(response,
                                     target_url,
                                     status_code=302,
                                     target_status_code=200)
        posts_after_test = list(Post.objects.order_by('pk').all())
        self.assertEqual(post_count, Post.objects.count(),
                         'Unauthorised user created post')
        self.assertEqual(posts_before_test, posts_after_test)

    def test_404(self):
        """
        Checking 404 answer of post page with wrong params
        """
        user404 = str(uuid1())[:5]
        id404 = randint(1000,2000)
        response = self.unauthorized_client.get(
            reverse('post', args=[user404, id404])
        )
        self.assertEqual(response.status_code, 404)
