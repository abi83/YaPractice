import os
from shutil import rmtree
from uuid import uuid1

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from django.urls import reverse

from posts.models import Post, Group, User, Follow


class FormsTests(TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Creating 'FirstUser', 'First Group', and 'First post' by 'FirstUser'
        Making a client, authorised as 'FirstUser'
        MEDIA_ROOT was change for test files delete in tearDown method
        """
        super().setUpClass()
        test_form_media_root = os.path.join(settings.MEDIA_ROOT,
                                            'test_temp_files')
        try:
            os.mkdir(test_form_media_root)
        except FileExistsError:
            pass
        settings.MEDIA_ROOT = test_form_media_root
        cls.first_user = User.objects.create_user(
            username=str(uuid1()))
        cls.followed_user = User.objects.create_user(username=str(uuid1()))
        cls.authorized_client = Client()
        cls.authorized_client.force_login(cls.first_user)
        cls.first_group = Group.objects.create(
            title=str(uuid1()),
            slug='first_slug'
        )
        cls.first_post = Post.objects.create(
            text=str(uuid1()),
            author=cls.first_user,
            group=cls.first_group,
        )

    @classmethod
    def tearDownClass(cls):
        """
        Cleaning up temporary files after test
        Set MEDIA_ROOT to default back
        """
        super().tearDownClass()
        rmtree(settings.MEDIA_ROOT)
        settings.MEDIA_ROOT = os.path.join(settings.BASE_DIR, 'media')

    def test_edit_post(self):
        """
        Testing if post-edit page saves data in database
        """
        post_to_edit = self.first_user.posts.first()
        new_group = Group.objects.create(title='One more', slug='one_more')
        new_text = str(uuid1())
        self.authorized_client.post(
            reverse('post-edit', args=[self.first_user.username,
                                       post_to_edit.pk], ),
            {'text': new_text, 'group': new_group.pk, },
            follow=True)
        post_to_edit.refresh_from_db()
        self.assertEqual(post_to_edit.text, new_text,
                         'Text wasnt edited')
        self.assertEqual(post_to_edit.group, new_group,
                         'Group wasnt edited')

    def test_authorised_user_new_post(self):
        """
        Authorised user can create posts with 'new-post' page
        """
        new_post_text = str(uuid1())
        response = self.authorized_client.post(
            reverse('new-post'),
            {'text': new_post_text,
             'group': self.first_group.pk, },
            follow=True)
        matches = 0
        for post in response.context['posts']:
            if (post.text == new_post_text and
                post.group == self.first_group and
                post.author == self.first_user):
                matches += 1
        self.assertEqual(matches, 1, 'Something wrong with new-post page')

    def test_foreign_post_edit_forbidden(self):
        """
        Testing foreign post editing prohibited
        """
        post_owner = User.objects.create_user(username='post_owner')
        tested_post = Post.objects.create(
            text='Uneditable post',
            author=post_owner, )
        cashed_text = Post.objects.get(pk=tested_post.pk).text
        target_url = reverse('post', args=[tested_post.author.username,
                                           tested_post.pk])
        response = self.authorized_client.post(
            reverse('post-edit', args=[tested_post.author.username,
                                       tested_post.pk]),
            {'text': 'Trying to edit', },
            follow=True)
        self.assertRedirects(response, target_url,
                             status_code=302, target_status_code=200)
        tested_post.refresh_from_db()
        self.assertEqual(cashed_text, tested_post.text,
                         'Someone can edit foreign posts')

    def test_new_comment_create(self):
        """
        Testing is comment appears after authorised client post request on
        add-comment page
        """
        comment_text = str(uuid1())
        response = self.authorized_client.post(
            reverse('add-comment', args=[self.first_post.author.username,
                                         self.first_post.pk]),
            {'text': comment_text},
            follow=True)
        self.assertIn(
            comment_text,
            [comment.text for comment in response.context_data['comments']]
        )

    def test_following_unfollowing_buttons(self):
        """
        Checking if Follow instance created and deleted with follow and
        unfollow buttons
        """
        # Deleting current following object if exists
        Follow.objects.filter(
            author=self.followed_user, user=self.first_user).delete()
        with self.subTest(msg='Follow button'):
            self.authorized_client.get(
                reverse('profile-follow', args=[self.followed_user.username]))
            self.assertTrue(
                Follow.objects.filter(author=self.followed_user,
                                      user=self.first_user).exists(),
                'Follow button works incorrectly')
        with self.subTest(msg='Unfollow button'):
            self.authorized_client.get(
                reverse('profile-unfollow', args=[self.followed_user.username]))
            self.assertFalse(
                Follow.objects.filter(author=self.followed_user,
                                      user=self.first_user).exists(),
                'Unfollow button works incorrectly')

    def test_followed_authors_post_appears_in_follow_list(self):
        """
        Checking if followed author post correctly appears on follow page
        """
        tested_post = Post.objects.create(
            text=str(uuid1()), author=self.followed_user)
        with self.subTest(
                msg='Check followed author post at follow_index page'):
            Follow.objects.get_or_create(
                author=self.followed_user, user=self.first_user)
            response = self.authorized_client.get(reverse('follow_index'))
            self.assertIn(
                tested_post.text,
                [post.text for post in response.context['posts']])
        with self.subTest(
                msg='Check unfollowed author post at follow_index page'):
            Follow.objects.filter(
                author=self.followed_user,
                user=self.first_user).delete()
            response = self.authorized_client.get(reverse('follow_index'))
            self.assertNotIn(
                tested_post.text,
                [post.text for post in response.context['posts']])

    def test_post_form_with_image_file(self):
        """
        Testing create a post form with a simple image
        """
        post_text = str(uuid1())
        pic_file_name = str(uuid1()) + '.gif'
        # anyway I couldn't feed a PIL Image object to SimpleUploadFile
        small_gif = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
            b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
            b'\x02\x4c\x01\x00\x3b'
        )
        self.authorized_client.post(
            reverse('new-post'),
            {'text': post_text,
             'group': self.first_group.pk,
             'image': SimpleUploadedFile(name=pic_file_name,
                                         content=small_gif,
                                         content_type='image/gif')
             },
        )
        new_post = Post.objects.get(text__exact=post_text)
        self.assertTrue(
            pic_file_name in new_post.image.name)

    def test_post_form_with_txt_file_error(self):
        """
        Testing create post form with txt file
        """
        post_text = str(uuid1())
        response = self.authorized_client.post(
            reverse('new-post'),
            {'text': post_text,
             'group': self.first_group.pk,
             'image': SimpleUploadedFile(name='test_txt.txt',
                                         content=b'These are the file contents',
                                         content_type='text/plain'),
             },)
        self.assertFalse(Post.objects.filter(text__exact=post_text).exists(),
                         'Post was created with txt file instead image')
        self.assertFormError(
            response, 'form', 'image',
            ['Загрузите правильное изображение. Файл, который вы загрузили, '
             'поврежден или не является изображением.'],
            msg_prefix='New-post form is valid with .txt file')
        self.assertEqual(
            response.context['form'].cleaned_data['text'], post_text,
            'Retry option is impossible. The PostForm is broken')
