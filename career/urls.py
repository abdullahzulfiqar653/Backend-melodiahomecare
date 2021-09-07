"""melodihomecare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('<slug:slug>/', views.branch, name="branch"),
    path('employee-benefits', views.benefits, name="benefits"),
    path('job-opening', views.job_opening, name="job_opening"),
    path('services-and-areas', views.areas, name="areas"),
    path('about', views.team, name="team"),
    path('apply-now', views.apply_now, name="apply_now"),
]
