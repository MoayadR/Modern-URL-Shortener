from django.shortcuts import render,redirect
from .models import short_url
from django.contrib.auth.decorators import login_required
from django.db.models import F  

# Create your views here.

@login_required(login_url="login")
def homepage(request):
    return render(request , 'URLs/home.html')

@login_required(login_url="login")
def myURLs(request):
    objects = short_url.objects.filter(user = request.user)
    return render(request , "URLs/my_urls.html" ,{"objects" : objects})

def visitURL(request, shortURL):
    object = short_url.objects.get(short_url = shortURL)
    object.visits = F('visits') +1
    object.save()
    return redirect(object.long_url)

def deleteURL(request , id):
    short_url.objects.get(id = id).delete()
    return redirect('my_urls')