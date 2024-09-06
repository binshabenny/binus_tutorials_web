from django.forms import ModelForm
from .models import BookSeat,Contact
from django import forms
from django.core.exceptions import ValidationError
from django.core import validators



class BookingForm(ModelForm):
    CLASS_CHOICES = [
        ('', 'Select A Class'), 
        ('Plus One Computer Science', 'Plus One Computer Science'),
        ('Plus One Computer Application', 'Plus One Computer Application'),
        ('Plus Two Computer Science', 'Plus Two Computer Science'),
        ('Plus Two Computer Application', 'Plus Two Computer Application'),
        ('B.Tech Computer Science', 'B.Tech Computer Science'),
    ]

    subject = forms.ChoiceField(choices=CLASS_CHOICES, widget = forms.Select(attrs={'class': 'custom-select border-0 px-4', 'style': 'height: 47px'}))

    class Meta:
        model = BookSeat
        fields = ['name', 'email', 'phone_number', 'subject']

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if len(name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters long.")
        return name
    
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phonenumber', 'subject', 'message']

    def clean_name(self):
        
        name = self.cleaned_data.get('name')

        if len(name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters long.")
        return name

    