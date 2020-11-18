import os
from shutil import rmtree
from uuid import uuid1

from django.conf import settings
from django.core.cache import cache
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from django.urls import reverse

from posts.models import Post, Group, User, Comment


class ViewsTests(TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Making unauthorised client
        Creating 'First Post', 'First Group' and 'FirstUser'
        MEDIA_ROOT was change for test files delete in tearDown method
        """
        super().setUpClass()
        test_view_media_root = os.path.join(settings.MEDIA_ROOT,
                                            'test_temp_files')
        try:
            os.mkdir(test_view_media_root)
        except FileExistsError:
            pass
        settings.MEDIA_ROOT = test_view_media_root
        cls.unauthorized_client = Client()
        cls.first_user = User.objects.create_user(
            username=str(uuid1()),
            first_name=str(uuid1()),
            last_name=str(uuid1()),
        )
        cls.first_group = Group.objects.create(
            title=str(uuid1()),
            slug='first_slug',
            description=str(uuid1()),
        )
        cls.first_post = Post.objects.create(
            text=str(uuid1()),
            group=cls.first_group,
            author=cls.first_user,
        )
        small_gif = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
            b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
            b'\x02\x4c\x01\x00\x3b'
        )
        cls.first_post.image = SimpleUploadedFile(
                name=str(uuid1()) + '.gif',
                content=small_gif,
                content_type='image/gif')
        cls.first_post.save()
        cls.post_check_urls = [
            reverse('posts'),
            reverse('post', args=[cls.first_post.author, cls.first_post.pk]),
            reverse('group-posts', args=[cls.first_group.slug]),
            reverse('profile', args=[cls.first_user.username]),
        ]

    @classmethod
    def tearDownClass(cls):
        """
        Cleaning up temporary files after test
        Set MEDIA_ROOT to default back
        """
        super().tearDownClass()
        rmtree(settings.MEDIA_ROOT)
        settings.MEDIA_ROOT = os.path.join(settings.BASE_DIR, 'media')

    def test_post_view_on_all_pages(self):
        """
        Checking if First Post content is available
        at posts page, author profile page, simple post and group pages
        """
        cache.clear()
        for url in self.post_check_urls:
            with self.subTest(url=url):
                response = self.unauthorized_client.get(url)
                self.assertTrue(
                    (self.first_post == response.context['post']) or
                    (self.first_post in response.context['posts']),
                    f'Page {url} dosnt contains post text')

    def test_img_tag_on_all_pages(self):
        """
        Checks <img> tag with "card-img" class in list of pages
        """
        cache.clear()
        for url in self.post_check_urls:
            with self.subTest(url=url):
                response = self.unauthorized_client.get(url)
                self.assertContains(response, '<img class="card-img"')

    def test_cache_index_page(self):
        """
        Checking correct cache work on index page
        """
        response_one = self.unauthorized_client.get(reverse('posts'))
        Post.objects.create(text='Cache check', author=self.first_user)
        response_two = self.unauthorized_client.get(reverse('posts'))
        cache.clear()
        response_three = self.unauthorized_client.get(reverse('posts'))
        self.assertEqual(response_one.content, response_two.content,
                         'Cache doesnt work')
        self.assertNotEqual(response_two.content, response_three.content,
                            'Couldnt clean the cache')

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

    def test_unauthorised_user_new_comment_redirect(self):
        """
        Checking post anf get methods requests for add-comment page
        with unauthorised client
        """
        target_url = reverse('login')+'?next='+reverse(
            'add-comment', args=[self.first_post.author.username,
                                 self.first_post.pk])
        comments_count = Comment.objects.all().count()
        responses = {
            'get': self.unauthorized_client.get(
                reverse('add-comment', args=[
                    self.first_post.author.username,
                    self.first_post.pk]),
                follow=False),
            'post': self.unauthorized_client.post(
                reverse('add-comment', args=[
                    self.first_post.author.username,
                    self.first_post.pk]),
                {'text': 'Test unauthorized user new comment'},
                follow=False)}
        for response in responses.values():
            with self.subTest(response=response):
                self.assertRedirects(
                    response,
                    target_url,
                    status_code=302,
                    target_status_code=200,
                    msg_prefix=f'Redirect for {response} fails')
        self.assertEqual(comments_count, Comment.objects.all().count())
