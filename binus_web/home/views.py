from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')

def classes(request):
    return render(request,'class.html')

def video_lectures(request):
    return render(request,'video.html')

def contact(request):
    return render(request,'contact.html')

