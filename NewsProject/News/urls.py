from django.urls import path, include

from News.views import index, get_category


urlpatterns = [
    path('', index, name='News'),
    path('shukik/', include('Shukik.urls')),
    path('category/<int:category_id>', get_category, name='Category')
]

