from django.shortcuts import render,redirect
from .models import Tutorial
from .models import Item
from .models import Pictures
from .forms import BookingForm
from django.contrib.auth.models import User


# Create your views here.


def index(request):  
    form = BookingForm() 

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()  # Saves the form data to the database
            return redirect('home')
        else:
            # If the form is not valid, stay on the page and show errors
            print(form.errors)
    
    
    tutorials = Tutorial.objects.all()
    videos = Item.objects.all()
    img = Pictures.objects.first()

    return render(request, 'index.html', {'tutorials': tutorials, 'videos': videos, 'img': img, 'form': form})


def about(request):
    img = Pictures.objects.first()
    return render(request,'about.html',{'img': img })

def classes(request):
    tutorials = Tutorial.objects.all()
    form  = BookSeat(request)
    return render(request, 'class.html', {'tutorials': tutorials, 'form': form,})

def video_lectures(request):
    return render(request,'video.html')

def contact(request):
    return render(request,'contact.html')


def video(request):
    obj = Item.objects.all()
    return render(request,'video_test.html',{'obj':obj})

