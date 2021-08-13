from mysite.image_processing import string_to_image
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json
def homepage(request):
    return render(request, 'home.html')

@csrf_exempt
def receive(request):
    #print(request.POST.get('image'))
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    image = body['image']
    print(image)
    string_to_image(image)
    return HttpResponse()



def save_to_json(request):
    return request()