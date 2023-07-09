from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', help_text='Максимум 150 символов', widget=forms.TextInput(attrs={'class': 'form-control'}))  # noqa: E501
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', help_text='', widget=forms.PasswordInput(attrs={'class': 'form-control'}))  # noqa: E501
    password2 = forms.CharField(label='Пароль', help_text='', widget=forms.PasswordInput(attrs={'class': 'form-control'}))  # noqa: E501
    captcha = CaptchaField()


    class Meta:
        model = User
        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-control'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control'}),
        #     'pasword1': forms.PasswordInput(attrs={'class': 'form-control'}),
        #     'pasword2': forms.PasswordInput(attrs={'class': 'form-control'}),

        # }
        fields = ('username', 'email', 'password1', 'password2')

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', help_text='Максимум 150 символов', widget=forms.TextInput(attrs={'class': 'form-control'}))  # noqa: E501
    password = forms.CharField(label='Пароль', help_text='', widget=forms.PasswordInput(attrs={'class': 'form-control'}))  # noqa: E501
    
