from . import views
from django.urls import path 

urlpatterns = [
    path('short-url/' ,views.createShortURL ),
]