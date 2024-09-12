# utils.py

from twilio.rest import Client

from django.conf import settings
from twilio.base.exceptions import TwilioRestException
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

def send_sms(to_phone_number, message):
   
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        msg = client.messages.create(
            body=message,
            from_=settings.TWILIO_PHONE_NUMBER,
            to=to_phone_number
        )
        return msg.sid
    


def book_seat_and_send_sms(form):
    """
    This helper function processes the booking form and sends an SMS notification.
    """
    form.save()  # Save form data to the database

    # Prepare SMS details
    user_name = form.cleaned_data['name']
    user_phone_number = form.cleaned_data['phone_number']
    message = f"New booking: {user_name} has booked a seat. Contact: {user_phone_number}"
    send_sms(settings.MY_PHONE_NUMBER, message)

