from django.http import JsonResponse 
from django.views.decorators.csrf import csrf_exempt
from URLs.models import server_counter , short_url
from django.core.files.images import ImageFile
import qrcode
import json

def base62Encryption(number : int):
    s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    result = ''
    counter = 0
    while(number > 0 and counter != 7):
        result = s[int(number % 62)] + result
        number //= 62
        counter += 1
    
    return result

def shortURLExist(user , longURL):
    if short_url.objects.filter(user = user , long_url = longURL).count() == 1:
        return True
    return False

def generateShortURL():
    counter = server_counter.objects.first()
    if(counter.counter <= counter.counter_limit):
        hashed = str(base62Encryption(counter.counter))
        counter.counter +=1
        counter.save() 
        return hashed
    return None

# Create your views here.
@csrf_exempt
def createShortURL(request):
    if request.method == "POST":
        bodyDict = json.loads(request.body)
        if shortURLExist(request.user , bodyDict["longURL"]):
            object = short_url.objects.get(user = request.user , long_url = bodyDict["longURL"])
            shortURL = object.short_url
        else:
            shortURL = generateShortURL()

            # qrCode  Generation
            img = qrcode.make('http://127.0.0.1:8000/' + shortURL)
            img.save(f'media/generatedQrCodes/{shortURL}.png')
            
            object = short_url.objects.create(user = request.user , long_url = bodyDict["longURL"] , short_url = shortURL)
            object.qrcode = ImageFile(open(f'media/generatedQrCodes/{shortURL}.png', "rb") , f'{shortURL}.png')     
            object.save()

        return JsonResponse({'shortURL' : shortURL})