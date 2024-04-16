from django import forms
from django.forms import DateTimeInput

from django_course_app.models import Client, Message, Newsletter

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class ClientForm(StyleFormMixin, forms.ModelForm):

    class Meta():
        model = Client
        exclude = ('owner',)
        fields = ['email', 'name','comment', 'is_active']


class MessageCreateForm(StyleFormMixin, forms.ModelForm):

    class Meta():
        model = Message
        exclude = ('owner',)
        fields = ['title', 'text']


class NewsletterCreateForm(StyleFormMixin, forms.ModelForm):

    class Meta():
        model = Newsletter
        fields =['start_date', 'interval', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'clients':
                field.widget.attrs['class'] = 'form-control'