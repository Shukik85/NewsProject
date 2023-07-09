from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import CreateView, DetailView, ListView
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from .forms import NewsForm
from .models import News, Category
from .utils import MyMixin


class HomeNews(ListView, MyMixin):
    model = News
    context_object_name = 'news'
    template_name = 'News/index.html'
    extra_context = {'title': 'Главная'}
    paginate_by = 2
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context
    
    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')
    

class NewsByCategory(ListView):
    model = News
    context_object_name = 'news'
    template_name = 'News/category.html'
    allow_empty = False
    paginate_by = 2
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id']).title
        return context
    
    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')
    
    
class ViewNews(DetailView):
    model = News
    template_name = 'News/news.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = News.objects.get(pk=self.kwargs['pk']).title
        return context
    
        
class AddNews(CreateView):
    form_class = NewsForm
    template_name = 'News/add_news.html'
    extra_context = {'title': 'Добавить новость'}
    login_url = 'admin/'

    

# Create your views here.
# def index(request):
#     news = News.objects.all()
#     context = {
#         'news': news,
#         'title': 'Список новостей'
#     }
#     return render(request, 'News/index.html', context=context)


# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     context = {
#         'news': news,
#         'category': category,
#         'title': category.title
#     }
#     return render(request, 'News/category.html', context=context)

# def view_news(request, news_id):
#     # news = News.objects.get(pk=news_id)
#     news = get_object_or_404(News, pk=news_id)
#     context = {
#         'news': news,
#         'title': news.title,
#     }
#     return render(request, 'News/news.html', context=context)

# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST, request.FILES)
#         if form.is_valid():
#             # news = form.save()
#             news = News.objects.create(**form.cleaned_data)
#             return redirect(news)
        
#     else:
#         form = NewsForm
#     context = {
#         'form': form,
#         'title': 'Добавить новость',
#     }
#     return render(request, 'News/add_news.html', context=context)
