from typing import Any, Dict
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, ListView, DetailView
from .models import Human, Profession
from .forms import HumanForm

class HumanViews(ListView):
    model = Human
    context_object_name = 'humans'
    template_name = 'Shukik/index.html'
    extra_context = {'title': 'Люди'}
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'ЛюдиКонтекст'
        return context
        
    

# def index(request):
#     humans = Human.objects.all()
#     profession = Profession.objects.all()
#     context = {
#         'humans': humans,
#         'title': 'Люди',
#         'profession': profession
#     }
#     return render(request, 'Shukik/index.html', context=context)


def get_profession(request, profession_id):
    humans = Human.objects.filter(profession_id=profession_id)
    profession = Profession.objects.get(pk=profession_id)
    context = {
        'humans': humans,
        'title': profession.title,
        'profession': profession
    }
    return render(request, 'Shukik/profession.html', context=context)

def view_human(request, human_id):
    # news = News.objects.get(pk=news_id)
    human = get_object_or_404(Human, pk=human_id)
    context = {
        'human': human,
        'title': human.name,
    }
    return render(request, 'Shukik/human.html', context=context)

def add_human(request):
    if request.method == 'POST':
        form = HumanForm(request.POST, request.FILES)
        if form.is_valid():
            human = form.save()
            # news = News.objects.create(**form.cleaned_data)
            return redirect(human)
        
    else:
        form = HumanForm
    context = {
        'form': form,
        'title': 'Добавить человека',
    }
    return render(request, 'Shukik/add_human.html', context=context)