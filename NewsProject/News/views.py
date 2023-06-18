from django.shortcuts import render
from .models import News, Category

# Create your views here.
def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей'
    }
    return render(request, 'News/index.html', context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'category': category,
        'title': 'Список новостей'
    }
    return render(request, 'News/category.html', context=context)
