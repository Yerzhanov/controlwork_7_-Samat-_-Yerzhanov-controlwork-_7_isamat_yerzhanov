from django.db import models
from django.contrib.auth.models import User
from django.db.models import TextChoices


class StatusChoice(TextChoices):
    ACTIVE = 'ACTIVE', 'Активна'
    BLOCKED = 'BLOCKED', 'Заблокировано'


class User_book(models.Model):
    name = models.CharField(max_length=128, verbose_name='Автор')
    email = models.EmailField(null=True, blank=True, verbose_name='Электронная почта')

    def __str__(self):
        return self.name


class GuestBook(models.Model):
    user = models.ForeignKey(to=User_book, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(blank=True, verbose_name='Текст записи')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    date_updated = models.DateTimeField(auto_now=True, null=True, verbose_name='Дата и время обновления')
    important = models.BooleanField(verbose_name='Важность', default=False)
    status = models.CharField(verbose_name='Статус', choices=StatusChoice.choices, max_length=20, default=StatusChoice.ACTIVE)

    def __str__(self):
        return f'Запись: {self.title} | Автор {self.user.name} | Электронная почта {self.user.email} | Cтатус {self.status}'
