from django import forms
from django.forms import fields, models, ModelForm, widgets
from .models import *


class ApplyForm(ModelForm):
    class Meta:
        model = Apply_Now
        fields = ['application_date', 'position', 'location', 'about', 'reffer', 'under_18', 'other_company_work', 'employeed', 'first_name',
                  'last_name', 'address1', 'address2', 'city', 'state', 'zip_code', 'email', 'phone', 'available', 'travel', 'cv', 'signature']
