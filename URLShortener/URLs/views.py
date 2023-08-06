from django.shortcuts import render
from .models import short_url

# Create your views here.


def homepage(request):
    return render(request , 'URLs/home.html')

def myURLs(request):
    objects = short_url.objects.filter(user = request.user)
    return render(request , "URLs/my_urls.html" ,{"objects" : objects})