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
        help_text='Описание долджно отражать смысл группы, ее содержание.',
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
    title = models.CharField(
        max_length=200,
        verbose_name='Название поста',
        help_text='Назовите пост так, чтобы его хотелось открыть.',
        null=True,
    )
    text = models.TextField(
        verbose_name='Текст вашего поста',
        help_text='Напишите сво интересную и захватывающую историю',
        null=False,
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name='Группа для вашего поста',
        help_text='Выберите группу, или оставьте пустым',
    )
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.text[:25] + '...'
