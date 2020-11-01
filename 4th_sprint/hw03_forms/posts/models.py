from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название группы',
    )
    slug = models.SlugField(
        unique=True,
        max_length=20,
        verbose_name='Часть URL адреса группы',
    )
    description = models.TextField(
        verbose_name='Описание группы',
        help_text='Напишите о чем эта группа, какие посты в ней будут',
    )
    active = models.BooleanField(
        default=True,
        verbose_name='Видимость группы на сайте',
    )

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title


class Post(models.Model):

    def default_title(self):
        words = self.text.split()
        return ' '.join(words[:4]) + '...'

    def save(self, *args, **kwargs):
        if not self.title:
            self.title = self.default_title()
        super(Post, self).save(*args, **kwargs)

    title = models.CharField(
        max_length=200,
        verbose_name='Название поста',
        help_text='Назовите пост или оставьте пустым',
        null=False,
    )
    text = models.TextField(
        verbose_name='Текст вашего поста',
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор поста',
        null=False,
        related_name='posts',
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name='Группа для вашего поста',
        help_text='Выберите группу или оставьте пустым',
    )

    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return f'Пост "{self.title}" от {self.pub_date}.'
