import datetime

from django.conf import settings
from django.core.mail import send_mail

from django_course_app.models import MailingAttempt, Client, Newsletter


def send_mail_now(schedule):

    message = schedule.message
    users = Newsletter.objects.get(id=schedule.id).clients.all()
    print(users)

    try:
        schedule.status = 3
        result = send_mail(
            subject=message.subject,
            message=message.text,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email for user in users],
            fail_silently=False,
        )
        print('sent')
        print([user.email for user in users])
        print(result)

        MailingAttempt.objects.create(
            schedule=schedule,
            status_of_last_attempt=True,
            server_response="Сообщение отправлено успешно"
        )

        print("Log created")
        if schedule.end_date and schedule.end_date <= datetime.date.today():
            # Если время рассылки закончилось, обновляем статус расписания на "завершено"
            schedule.status = 'f'
        schedule.save()

    except Exception as e:
        MailingAttempt.objects.create(
            schedule=schedule,
            status_of_last_attempt=False,
            server_response=f"Ошибка при отправке сообщения: {e}"
        )
        print('Schedule failed, check logs')
        schedule.status = 'e'
        schedule.save()