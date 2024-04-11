from django.contrib import admin

from django_course_app.models import Client, Message, MailingAttempt, Newsletter


@admin.register(Client)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'interval', 'mailing_status')


@admin.register(MailingAttempt)
class MailingAttemptAdmin(admin.ModelAdmin):
    list_display = ('date_of_last_attempt', 'status_of_last_attempt', 'server_response')
    list_filter = ('date_of_last_attempt',)
