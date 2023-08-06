from django.shortcuts import render , redirect
from django.contrib.auth.models import User  
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login , logout 
from django.contrib import messages
from .forms import UserSignUpForm
# Create your views here.

def logIn(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request , username = username , password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,"Login Credentials is wrong please try again...")
            return redirect('login')

    # GET method
    return render(request , "Access/login.html")

def logOut(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            plainPassword = form.cleaned_data['password']
            form.instance.password = make_password(plainPassword)
            user = form.save()
            login(request , user)
            return redirect('home')
    else:
        form = UserSignUpForm()
    
    context = {'form': form}
    return render(request , 'Access/register.html' , context=context)