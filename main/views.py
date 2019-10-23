from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
import re
import base64

dataUrlPattern = re.compile('data:image/(png|jpeg);base64,(.*)$')

# Create your views here.
def home(request):
    context = {
        "title":"CaptureCam | Home",
    }
    return render(request,'index.html',context)

def file1(request):
    context = {
        "title":"CaptureCam | Home",
    }
    return render(request,'file.html',context)

def captureImage(request):
    dict = {}
    context = {
        "title":"HOME",
    }
    if request.method == 'POST':
        image = request.POST.get('image')
        # imageData = dataUrlPattern.match(image).group(2)
        # ImageData = base64.b64decode(imageData)
        # print(ImageData)
    return HttpResponse("DONE")