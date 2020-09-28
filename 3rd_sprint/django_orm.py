# Создайте модель мероприятия для сайта-афиши.
# У модели должны быть такие поля:
# Название мероприятия (name), не больше 200 символов
# Дата и время проведения мероприятия (start_at)
# Описание мероприятия (description)
# Адрес электронной почты организатора мероприятия (contact)
# Пользователь, который создал мероприятие (author,
# related_name этого поля должно быть events)
# Название места проведения мероприятия (location), не более 400 символов

from django.db import models
from django.contrib.auth import get_user_model

class Event(models.Model):
    name = models.CharField(max_length=200)
    start_at = models.DateTimeField('event published', auto_now_add=True)
    description = models.TextField
    contact = models.EmailField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                               related_name="event_author")
    location = models.CharField(max_length=400)
