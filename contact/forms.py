from django import forms
from django.forms import fields, models
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = {'first_name','last_name','address','city','state','zip_code','email','phone','questions'}
