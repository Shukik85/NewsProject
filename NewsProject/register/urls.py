from django.urls import path
from register.views import user_login, register, user_logout

urlpatterns = [
    
    path('register/', register, name='Register'),
    path('login/', user_login, name='Login'),
    path('logout/', user_logout, name='Logout'),
]
