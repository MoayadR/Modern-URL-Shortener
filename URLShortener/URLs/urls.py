from . import views
from django.urls import path 

urlpatterns = [
    path('' , views.homepage , name='home'),
    path('<shortURL>/' , views.visitURL , name='visit'),
    path('url/my_urls/' , views.myURLs , name='my_urls'),
    path('url/delete/<uuid:id>' , views.deleteURL , name="delete")
]