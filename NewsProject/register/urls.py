from django.urls import path
from register.views import login, register

urlpatterns = [
    
    path('register/', register, name='Register'),
    path('login/', login, name='Login')
]
