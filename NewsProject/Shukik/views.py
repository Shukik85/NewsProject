from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, ListView, DetailView
from .models import Human, Profession
from .forms import HumanForm

class HumanViews(ListView):
    model = Human
    context_object_name = 'human'
    template_name = 'Shukik/index.html'
    extra_context = {'title': 'Люди'}
    paginate_by = 2
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Люди'
        return context
    
    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().select_related('profession')
        
    
class HumanProfession(ListView):
    context_object_name = 'human'
    template_name = 'Shukik/profession.html'
    paginate_by = 2
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.profession.title
        return context

    def get_queryset(self):
        self.profession = get_object_or_404(Profession, pk=self.kwargs['pk'])
        return Human.objects.filter(profession=self.profession).select_related('profession')
    
    
class HumanPerson(DetailView):
    model = Human
    template_name = 'Shukik/human.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Human.objects.get(pk=self.kwargs['pk']).name
        return context
    
        
class AddHuman(CreateView):
    form_class = HumanForm
    template_name = 'Shukik/add_human.html'
    extra_context = {'title': 'Добавить человека'}
    
    
# def index(request):
#     humans = Human.objects.all()
#     profession = Profession.objects.all()
#     context = {
#         'humans': humans,
#         'title': 'Люди',
#         'profession': profession
#     }
#     return render(request, 'Shukik/index.html', context=context)


# def get_profession(request, profession_id):
#     human = Human.objects.filter(pk=profession_id)
#     profession = Profession.objects.get(pk=profession_id)
#     context = {
#         'human': human,
#         'title': profession.title,
#         'profession': profession
#     }
#     return render(request, 'Shukik/profession.html', context=context)

# def view_human(request, pk):
#     # news = Human.objects.get(pk=human_id)
#     human = get_object_or_404(Human, pk=pk)
#     context = {
#         'human': human,
#         'title': human.name,
#     }
#     return render(request, 'Shukik/human.html', context=context)

# def add_human(request):
#     if request.method == 'POST':
#         form = HumanForm(request.POST, request.FILES)
#         if form.is_valid():
#             human = form.save()
#             # news = News.objects.create(**form.cleaned_data)
#             return redirect(human)
        
#     else:
#         form = HumanForm
#     context = {
#         'form': form,
#         'title': 'Добавить человека',
#     }
#     return render(request, 'Shukik/add_human.html', context=context)