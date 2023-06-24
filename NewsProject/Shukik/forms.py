from django import forms
from .models import Human
import re
from django.core.exceptions import ValidationError


class HumanForm(forms.ModelForm):
    
    def clean_name(self):
        name = self.cleaned_data['name']
        if re.match(r'\d', name):
            raise ValidationError('Имя не должно начинаться с цифры')
        return name
    # name
    # surname
    # email
    # info
    # photo
    # is_admin 
    # profession
    
    class Meta:
        model = Human
        fields = ['name', 'surname', 'email', 'info', 'photo', 'profession',]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'info': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'profession': forms.Select(attrs={'class': 'form-control'}),
        }
    
    # name = forms.CharField(max_length=150, label='Заголовок', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # photo = forms.ImageField(label='Фото', required=False)
    # content = forms.CharField(label='Новость', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    # is_published = forms.BooleanField(initial=True, label='Публикация')
    # category = forms.ModelChoiceField(queryset=Profession.objects.all(), label='Категория', empty_label='Выберите категорию', widget=forms.Select(attrs={'class': 'form-control'}))
    