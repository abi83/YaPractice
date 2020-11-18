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
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название поста',
        help_text='Назовите пост',
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
        verbose_name='Группа для поста',
        help_text='Выберите группу или оставьте пустым',
    )
    image = models.ImageField(
        upload_to='posts/',
        blank=True,
        null=True,
        verbose_name='Изображение для поста',
        help_text='Только файлы изображений',
    )
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        post_title = self.title
        post_pub_date = self.pub_date
        return f'Пост "{post_title}" от {post_pub_date:%d.%m.%Y}.'

    def default_title(self):
        words = self.text.split()
        return ' '.join(words[:4]) + '...'

    def save(self, *args, **kwargs):
        if not self.title:
            self.title = self.default_title()
        super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Пост с комментарием',
    )
    author = models.ForeignKey(
        User,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор комментария',
    )
    text = models.TextField(
        verbose_name='Текст комментария',
    )
    created = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
    )
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        comment_text = self.text[:20]
        comment_pub_date = self.created
        return f'Комментарий {comment_text}... от {comment_pub_date:%d.%m.%Y}.'


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Читатель',
        related_name='follower',
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        related_name='following',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(fields=['user', 'author'],
                                    name='twice_follow_impossible')]
