
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('Login')
        else:
            messages.error(request, 'Ошибка регистрации.')
    else:
        form = UserCreationForm()
    return render(request, 'reg/register.html', {'form': form, 'title': 'Регистрация'})

def login(request):
    form = UserChangeForm()
    return render(request, 'reg/login.html', {'form': form, 'title': 'Вход'})