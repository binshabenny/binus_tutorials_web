from django.shortcuts import render
from .models import Tutorial

# Create your views here.
def index(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'index.html', {'tutorials': tutorials})


def about(request):
    return render(request,'about.html')

def classes(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'class.html', {'tutorials': tutorials})

def video_lectures(request):
    return render(request,'video.html')

def contact(request):
    return render(request,'contact.html')

