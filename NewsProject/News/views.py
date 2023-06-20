from django.shortcuts import get_object_or_404, render
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

def view_news(request, news_id):
    # news = News.objects.get(pk=news_id)
    news = get_object_or_404(News, pk=news_id)
    context = {
        'news': news,
        'title': news.title
    }
    return render(request, 'News/news.html', context=context)
