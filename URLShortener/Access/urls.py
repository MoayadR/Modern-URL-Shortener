from . import views
from django.urls import path 

urlpatterns = [
    path('login/' , views.logIn , name='login'),
    path('register/' , views.register , name='register'),
    path('logout/' , views.logOut , name='logout'),
]