"""
Урок8. Регистрация модели в админке:
Перед вами альфа-версия проекта для любителей хранить музыку на компакт-дисках. Пока что в нем есть только модель CD для хранения информации об
альбомах. Модель вы найдете в приложении practice: practice/models.py
Cконфигурируйте модель так, чтобы администратору сайта было удобно работать с ней в админке.
В админ-зоне должны быть видны такие поля:
название альбома
дата релиза
артист
жанр
Должна быть фильтрация записей по полям:
дата релиза
жанр
Пустые поля в записях должны заполняться строкой -пусто-
После выполнения задания задеплойте проект в тренажёре (кнопка Задеплоить), затем откройте в новом окне браузера свой проект
(по ссылке вверху справа в интерфейсе тренажёра), перейдите на страницу /admin и авторизуйтесь: логин admin, пароль admin.
В админке проверьте результат своей работы.
"""

# models.py

from django.db import models

# Create your models here.
GENRE_CHOICES = (
    ("R", "Рок"),
    ("E", "Электроника"),
    ("P", "Поп"),
    ("C", "Классика"),
    ("O", "Саундтреки"),
)


class CD(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    artist = models.CharField(max_length=40)
    date = models.DateField()
    genre = models.CharField(max_length=1, choices=GENRE_CHOICES)


# admin.py
from django.contrib import admin
from .models import CD


class CDAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "date", "artist", "genre")
    search_fields = ("text",)
    list_filter = ("date", "genre")
    empty_value_display = "-пусто-"


admin.site.register(CD, CDAdmin)
