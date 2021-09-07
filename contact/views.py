from django.shortcuts import render, redirect
from .forms import *
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings
# Create your views here.


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contacts = form.save()
            subject = "Website Inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'address': form.cleaned_data['address'],
                'city': form.cleaned_data['city'],
                'state': form.cleaned_data['state'],
                'zip_code': form.cleaned_data['zip_code'],
                'email': form.cleaned_data['email'],
                'phone': form.cleaned_data['phone'],
                'questions': form.cleaned_data['questions'],
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message, 'admin@example.com',
                          [settings.EMAIL_HOST_USER])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("/")

    form = ContactForm()
    return render(request, "contact-us.html", {'form': form})
