from django.urls import path
from Shukik.views import index, get_profession


urlpatterns = [
    path('', index, name='Shukik'),
    path('profession/<int:profession_id>', get_profession, name='Profession')
]
