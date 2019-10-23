from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        "title":"CaptureCam | Home"
    }
    return render(request,'index.html',context)