from django.forms import ModelForm
from django import forms

from .models import BookSeat,Contact,Tutorial



class BookingForm(forms.ModelForm):
    class Meta:
        model = BookSeat
        fields = ['name', 'email', 'phone_number', 'place', 'subject']

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        self.fields['subject'].queryset = Tutorial.objects.all()
        self.fields['subject'].widget = forms.Select(attrs={'class': 'custom-select border-0 px-4', 'style': 'height: 47px'})

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

    