from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Nursing_Service, Care_Service
# Create your views here.


def home(request):
    return render(request, 'home.html')


def nursing_service(request):
    nurs_service = Nursing_Service.objects.all()
    return render(request, 'nursing-service.html', {'service': nurs_service})


def home_care(request):
    home_car = Care_Service.objects.all()
    return render(request, 'home-care-nursing.html', {'service': home_car})
