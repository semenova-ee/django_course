from django import forms
from django_course_app.models import Client, Message, Newsletter


class ClientForm(forms.ModelForm):

    class Meta():
        model = Client
        fields = ['email', 'name','comment']


class MessageCreateForm(forms.ModelForm):

    class Meta():
        model = Message
        fields = ['title', 'text']


class NewsletterCreateForm(forms.ModelForm):

    class Meta():
        model = Newsletter
        fields =['start_date', 'interval', 'mailing_status']
