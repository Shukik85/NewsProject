from dataclasses import fields
from django import forms
from .models import Category, News
import re
from django.core.exceptions import ValidationError
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User


# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')

class NewsForm(forms.ModelForm):
    
    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Заголовок не должен начинаться с цифры')
        return title
    
    
    class Meta:
        model = News
        fields = ['title', 'content', 'photo', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
    
    # title = forms.CharField(max_length=150, label='Заголовок', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))  # noqa: E501
    # photo = forms.ImageField(label='Фото', required=False)
    # content = forms.CharField(label='Новость', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))  # noqa: E501
    # is_published = forms.BooleanField(initial=True, label='Публикация')
    # category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='Выберите категорию', widget=forms.Select(attrs={'class': 'form-control'}))  # noqa: E501
    