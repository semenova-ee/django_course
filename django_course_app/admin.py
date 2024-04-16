from django.contrib import admin

from django_course_app.models import Client, Message, MailingAttempt, Newsletter


@admin.register(Client)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_active', 'created_at')
    list_filter = ('created_at',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')
    list_filter = ('created_at',)


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'interval', 'status')
    list_filter = ('start_date',)


@admin.register(MailingAttempt)
class MailingAttemptAdmin(admin.ModelAdmin):
    list_display = ('date_of_last_attempt', 'status_of_last_attempt', 'server_response', 'schedule')
    list_filter = ('date_of_last_attempt',)
