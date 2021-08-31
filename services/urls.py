from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('nursing-service', views.nursing_service, name='nursing_service'),
    path('home-care-nursing', views.home_care, name='home_care'),
]
