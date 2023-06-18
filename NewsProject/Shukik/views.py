from django.shortcuts import render
from .models import Human, Profession


def index(request):
    users = Human.objects.all()
    profession = Profession.objects.all()
    context = {
        'users': users,
        'title': 'Список пользователей',
        'profession': profession
    }
    return render(request, 'Shukik/index.html', context=context)


def get_profession(request, profession_id):
    users = Human.objects.filter(profession_id=profession_id)
    profession = Profession.objects.get(pk=profession_id)
    context = {
        'users': users,
        'title': 'Список пользователей',
        'profession': profession
    }
    return render(request, 'Shukik/profession.html', context=context)
