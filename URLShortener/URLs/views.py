from django.shortcuts import render

# Create your views here.

def base62Encryption(number : int):
    s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    result = ''
    counter = 0
    while(number > 0 and counter != 7):
        result = s[int(number % 62)] + result
        number //= 62
        counter += 1
    
    return result


def homepage(request):
    return render(request , 'URLs/home.html')