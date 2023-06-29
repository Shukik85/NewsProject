from django.urls import path
# from Shukik.views import index, get_profession, view_human, add_human
from Shukik.views import HumanViews, HumanProfession, HumanPerson, AddHuman


urlpatterns = [
    path('',  HumanViews.as_view(), name='Shukik'),
    path('profession/<int:pk>', HumanProfession.as_view(), name='Profession'),
    path('<int:pk>', HumanPerson.as_view(), name='Human'),
    path('human/add_human', AddHuman.as_view(), name='Add_human')
    
    # path('', index, name='Shukik'),
    # path('profession/<int:profession_id>', get_profession, name='Profession'),
    # path('<int:pk>', view_human, name='Human'),
    # path('human/add_human', add_human, name='Add_human')
]
