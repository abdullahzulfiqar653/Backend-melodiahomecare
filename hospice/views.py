from django.shortcuts import render
from .models import *
# Create your views here.
def what_is_hospice(request):
    hos = Hospice.objects.all()
    return render(request, 'what-is-hospice.html', {'hospice':hos})

def question(request):
    frequently = FAQ.objects.all()
    return render(request,'faq.html', {'faq':frequently})