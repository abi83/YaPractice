from django.test import TestCase, Client
from django.urls import reverse
from uuid import uuid1

from posts.models import Post, Group, User


class FormsTests(TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Creating 'FirstUser', 'First Group', and 'First post' by 'FirstUser'
        Making a client, authorised as 'FirstUser'
        """
        super().setUpClass()
        cls.first_user = User.objects.create_user(username='FirstUser')
        cls.authorized_client = Client()
        cls.authorized_client.force_login(cls.first_user)
        cls.first_group = Group.objects.create(
            title='first_group',
            slug='first_slug'
        )
        cls.first_post = Post.objects.create(
            text='SimplePost',
            author=cls.first_user,
            group=cls.first_group,
        )

    def test_edit_post(self):
        """
        Testing if post_edit page saves data in database
        """
        post_to_edit = self.first_user.posts.first()
        new_group = Group.objects.create(title='One more', slug='another')
        new_text = 'Edited post'
        self.authorized_client.post(
            reverse('post_edit', args=[self.first_user.username,
                                       post_to_edit.pk], ),
            {'text': new_text, 'group': new_group.pk, },
            follow=True)
        post_to_edit.refresh_from_db()
        self.assertEqual(post_to_edit.text, new_text,
                         'Text wasnt edited')
        self.assertEqual(post_to_edit.group, new_group,
                         'Gruop wasnt edited')

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
            author=post_owner,)
        cashed_text = Post.objects.get(pk=tested_post.pk).text
        target_url = reverse('post', args=[tested_post.author.username,
                                           tested_post.pk])
        response = self.authorized_client.post(
            reverse('post_edit', args=[tested_post.author.username,
                                       tested_post.pk]),
            {'text': 'Trying to edit', },
            follow=True)
        self.assertRedirects(response, target_url,
                             status_code=302, target_status_code=200)
        tested_post.refresh_from_db()
        self.assertEqual(cashed_text, tested_post.text)
