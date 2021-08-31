from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Nursing_Service, Care_Service, Aid_Service, Homemaking_Service,Assistant_Service
# Create your views here.


def home(request):
    return render(request, 'home.html')


def nursing_service(request):
    nurs_service = Nursing_Service.objects.all()
    return render(request, 'nursing-service.html', {'service': nurs_service})


def home_care(request):
    home_car = Care_Service.objects.all()
    return render(request, 'home-care-nursing.html', {'service': home_car})


def health_aide(request):
    health_aid = Aid_Service.objects.all()
    return render(request, 'home-health-aide.html', {'service': health_aid})

def personal_assistant(request):
    assistant = Assistant_Service.objects.all()
    return render(request, 'personal-care-assistant.html', {'service': assistant})

def home_making(request):
    homemaking = Homemaking_Service.objects.all()
    return render(request, 'homemaking-services.html', {'service': home_making})
