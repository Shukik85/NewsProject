from django.urls import path, include

from News.views import HomeNews, NewsByCategory, ViewNews,AddNews
#from News.views import index, get_category, view_news,add_news, test



urlpatterns = [
    path('', HomeNews.as_view(), name='News'),
    path('category/<int:category_id>', NewsByCategory.as_view(), name='Category'),
    path('<int:pk>', ViewNews.as_view(), name='News'),
    path('news/add_news', AddNews.as_view(), name='Add_news'),
    path('shukik/', include('Shukik.urls')),
    
    # path('test/', test, name='Test'),    
    # path('', index, name='News'),
    # path('category/<int:category_id>', get_category, name='Category'),
    # path('<int:news_id>', view_news, name='News'),
    # path('news/add_news', add_news, name='Add_news')
]
