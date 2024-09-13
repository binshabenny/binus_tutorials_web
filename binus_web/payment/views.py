from django.conf import settings
from django.shortcuts import render, get_object_or_404
from home.models import BookSeat  # Assuming you have BookSeat model for bookings
import razorpay
from django.shortcuts import render,redirect

def payment_page(request, order_id, fee):
    # Retrieve the booking based on the order_id
    booking = get_object_or_404(BookSeat, order_id=order_id)

    # Pass the required Razorpay data and booking details to the template
    context = {
        'order_id': order_id,
        'fee': int(fee) * 100,  # Convert fee to paisa (Razorpay accepts amounts in paisa)
        'RAZORPAY_KEY_ID': settings.RAZORPAY_KEY_ID,  # Fetch Razorpay Key ID from settings
        'booking': booking,  # Pass the booking object to access name and email
    }
    return render(request, 'payment.html')

