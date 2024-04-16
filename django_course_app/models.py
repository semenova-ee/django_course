from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}

class Client(models.Model):
    email = models.EmailField(max_length=200,null=True)
    name = models.CharField(max_length=200, null=True)
    comment = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    is_active = models.BooleanField(default=True, verbose_name='Активность')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Message(models.Model):
    title = models.CharField(max_length=200, verbose_name='Тема сообщения')
    text = models.TextField(verbose_name='Текст сообщения')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL,  verbose_name='Владелец', **NULLABLE)

    def __str__(self):
        return f'{self.title} {self.text}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Newsletter(models.Model):
    INTERVALS_CHOICES = (
        (1, 'DAILY'),
        (2, 'WEEKLY'),
        (3, 'MONTHLY'),
        (4, 'ONCE')
    )

    STATUS_CHOICES = (
        (1, 'CREATED'),
        (2, 'COMPLETED'),
        (3, 'LAUNCHED'),
    )

    clients = models.ManyToManyField(Client, verbose_name='Клиенты рассылки')
    start_date = models.DateTimeField(verbose_name='Начало рассылки')
    end_date = models.DateTimeField(verbose_name='Окончание рассылки')
    interval = models.PositiveSmallIntegerField(choices=INTERVALS_CHOICES, null=True)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, null=True)
    message = models.OneToOneField(Message, on_delete=models.CASCADE,verbose_name='Сообщение', null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Владелец', **NULLABLE)
    next_try = models.DateTimeField(verbose_name='Попытка следующей отправки', **NULLABLE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.start_date} - {self.status}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class MailingAttempt(models.Model):
    date_of_last_attempt = models.DateTimeField(auto_now=True, verbose_name='Дата и время последней попытки')
    status_of_last_attempt = models.BooleanField(default=False, verbose_name='Статус последний попытки')
    server_response = models.TextField(verbose_name='Ответ сервера', **NULLABLE)
    schedule = models.ForeignKey(Newsletter, on_delete=models.CASCADE, verbose_name='Расписание', **NULLABLE)

    def __str__(self):
        return f'{self.date_of_last_attempt} - {self.status_of_last_attempt}'

    class Meta:
        verbose_name = 'Логи рассылки'
        verbose_name_plural = 'Логи рассылок'