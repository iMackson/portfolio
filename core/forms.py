from django import forms
from phone_field import PhoneField
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


class ContactForm(forms.Form):
    name = forms.CharField(required=True, max_length=500, label='Name')
    email_address = forms.EmailField(required=True, max_length=500, label='Email Address')
    country = CountryField(blank_label='Select country').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={
        'placeholder': 'Enter your comment here.'
    }))