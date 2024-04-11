from django.db import models
# from django.conf import settings
# from django.core.mail import send_mail


class Message(models.Model):
    title = models.CharField(max_length=200, null=True)
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
        (1, 'CREATED'),
        (2, 'COMPLETED'),
        (3, 'LAUNCHED')
    )

    start_date = models.DateTimeField(null=True)
    interval = models.PositiveSmallIntegerField(choices=INTERVALS_CHOICES, null=True)
    mailing_status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, null=True)
    message = models.OneToOneField(Message, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.start_date} - {self.mailing_status}'


class MailingAttempt(models.Model):
    date_of_last_attempt = models.DateTimeField(null=True)
    status_of_last_attempt = models.BooleanField(null=True)
    server_response = models.TextField(null=True)

    def __str__(self):
        return f'{self.date_of_last_attempt} - {self.status_of_last_attempt}'


class Client(models.Model):
    email = models.EmailField(max_length=200,null=True)
    name = models.CharField(max_length=200, null=True)
    comment = models.TextField(null=True)
    newsletter = models.ForeignKey(Newsletter, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

#
# def send_message():
#     clients = Client.objects.all()
#
#     try:
#         Newsletter.mailing_status = '3'
#         result = send_mail(
#             subject=Message.title,
#             message=Message.text,
#             from_email=settings.EMAIL_HOST_USER,
#             clients_list=[client.email for client in clients],
#         )
#
#         MailingAttempt.objects.create(
#             status_of_last_attempt=True,
#             server_response="Сообщение отправлено",
#         )
#     except Exception as e:
#         MailingAttempt.objects.create(
#             status_of_last_attempt=False,
#             server_response=f"Ошибка при отправке сообщения: {e}"
#         )
#         print('Schedule failed, check logs')
