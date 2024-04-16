from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django_course_app.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Скрытие лишних подсказок
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''


class UserProfileForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Скрытие поля password
        self.fields['password'].widget = forms.HiddenInput()


class UserForManagerForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'is_active',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Делаем поля не доступными к редактированию.
        self.fields['email'].widget.attrs['readonly'] = True
        self.fields['first_name'].widget.attrs['readonly'] = True
        self.fields['last_name'].widget.attrs['readonly'] = True

        # Добавление чекбокса для is_active
        self.fields['is_active'].widget = forms.CheckboxInput()

        # Скрытие поля password
        self.fields['password'].widget = forms.HiddenInput()