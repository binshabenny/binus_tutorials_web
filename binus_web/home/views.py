from django.shortcuts import render,redirect
from .models import Tutorial
from .models import Item
from .models import Pictures
from .forms import BookingForm,ContactForm
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from .utils import send_sms




# Create your views here.


def index(request):  
    form = BookingForm() 

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            
            form.save()
            user_name = form.cleaned_data['name']
            user_phone_number = form.cleaned_data['phone_number']
            message = f"New booking: {user_name} has booked a seat. Contact: {user_phone_number}"
            
            # Send SMS to your phone number
            send_sms(settings.MY_PHONE_NUMBER, message)  # Saves the form data to the database
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
    
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
      
            form.save()  # Saves the form data to the database
            return redirect('class')
        else:
            print(form.errors)  # If the form is not valid, stay on the page and show errors
    else:
        form = BookingForm()  # Initialize the empty form for GET request
    
    tutorials = Tutorial.objects.all()
    return render(request, 'class.html', {'tutorials': tutorials, 'form': form})

def video_lectures(request):
    return render(request,'video.html')

def contact(request):

    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Thank you for contacting us!') # Saves the form data to the database
            return redirect('contact')  # Redirect after successful form submission
        else:
            print(form.errors)  # For debugging purposes, show form errors in console

    return render(request, 'contact.html', {'form': form})


def video(request):
    obj = Item.objects.all()
    return render(request,'video_test.html',{'obj':obj})

