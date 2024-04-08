from django.db import models


class Client(models.Model):
    email = models.EmailField(null=True)
    name = models.CharField(max_length=200, null=True)
    comment = models.TextField(null=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    title = models.CharField(null=True)
    text = models.TextField(null=True)

    def __str__(self):
        return f'{self.title} {self.text}'


class Newsletter(models.Model):
    INTERVALS_CHOICES = (
        (1, 'DAILY'),
        (2, 'WEEKLY'),
        (3, 'MONTHLY')
    )

    STATUS_CHOICES = (
        (1, 'COMPLETED'),
        (2, 'CREATED'),
        (3, 'LAUNCHED')
    )

    start_date = models.DateTimeField(null=True)
    interval = models.PositiveSmallIntegerField(choices=INTERVALS_CHOICES, null=True)
    mailing_status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, null=True)

    def __str__(self):
        return f'{self.start_date} - {self.mailing_status}'


class MailingAttempt(models.Model):
    date_of_last_attempt = models.DateTimeField(null=True)
    status_of_last_attempt = models.BooleanField(null=True)
    server_response = models.TextField(null=True)

    def __str__(self):
        return f'{self.date_of_last_attempt} - {self.status_of_last_attempt}'
