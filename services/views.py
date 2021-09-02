from django.http.response import HttpResponse
from django.shortcuts import render
from .models import *
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
    return render(request, 'personal-care-assistance.html', {'service': assistant})


def home_making(request):
    homemaking = Homemaking_Service.objects.all()
    return render(request, 'homemaking-services.html', {'service': home_making})


def therapy(request):
    thrpy = Therapy_Service.objects.all()
    return render(request, 'therapy.html', {'service': thrpy})


def iv_therapy(request):
    iv = IV_Therapy_Service.objects.all()
    return render(request, 'IV-therapy.html', {'service': iv})


def interpretive(request):
    inter = Interpretive_Service.objects.all()
    return render(request, 'interpretive-services.html', {'service': inter})


def independent_living(request):
    indp_living = Living_Skills_Service.objects.all()
    return render(request, 'independent-living-skills.html', {'service': indp_living})


def companion(request):
    cmp = Companion_Service.objects.all()
    return render(request, 'companion.html', {'service': cmp})


def respite(request):
    resp = Respite_Service.objects.all()
    return render(request, 'respite.html', {'service': resp})


def social_service(request):
    social = Social_Service.objects.all()
    return render(request, 'social-service.html', {'service': social})


def hospice(request):
    hspic = Hospice_Service.objects.all()
    return render(request, 'hospice.html', {'service': hspic})
