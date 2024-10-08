from django.shortcuts import render,redirect
from .models import Tutorial
from .models import Item
from .models import Pictures
from .models import BookSeat
from .forms import BookingForm,ContactForm
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail, get_connection
from .utils import book_seat_and_send_sms
import razorpay
import ssl



razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))


# Create your views here.


def index(request):  
    form = BookingForm() 

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            
            book_seat_and_send_sms(form)  # Saves the form data to the database
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
    return render(request, 'class.html' ,{'tutorials': tutorials})





def video_lectures(request):
    return render(request,'video.html')

def contact(request):

    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save() 

            
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            email_subject = f"New Contact Form Submission: {subject}"
            email_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            from_email = email  # Use the user's email as the sender

            send_mail(
                email_subject,          # Subject
                email_message,          # Message
                from_email,             # From (user's email)
                ['binuscomputer@gmail.com'],  # To (replace with your own email)
                fail_silently=False,
            )

            messages.success(request, 'Thank you for contacting us!') # Saves the form data to the database
            return redirect('contact')  # Redirect after successful form submission
        else:
            print(form.errors)  # For debugging purposes, show form errors in console

    return render(request, 'contact.html', {'form': form})


def video(request):
    obj = Item.objects.all()
    return render(request,'video_test.html',{'obj':obj})


def join_now(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        
        if form.is_valid():
            booking = form.save()  # Saves the form data to the database
            book_seat_and_send_sms(form)

            try:
                # Fetch the related Tutorial based on the subject name
                tutorial = Tutorial.objects.get(title=booking.subject)
            except Tutorial.DoesNotExist:
                form.add_error('subject', 'Invalid subject selected.')
                return render(request, 'join_now.html', {'form': form})
            
            fee = int(tutorial.tuition_fee * 100)  # Convert to paisa
            
            # Create Razorpay order
            order_data = {
                'amount': fee,
                'currency': 'INR',
                'payment_capture': '1',
            }
            order = razorpay_client.order.create(data=order_data)
            booking.order_id = order['id']
            booking.save()
            
            # Redirect to payment page
            return redirect('payment_page', order_id=booking.order_id, fee=fee)
        else:
            print(form.errors)  # If the form is not valid, stay on the page and show errors
    else:
        form = BookingForm()
    
    return render(request, 'join_now.html', {'form': form})


