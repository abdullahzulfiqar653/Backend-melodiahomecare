from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('nursing-service', views.nursing_service, name='nursing_service'),
    path('home-care-nursing', views.home_care, name='home_care'),
    path('home-health-aide', views.health_aide, name='health_aide'),
    path('home-making-services', views.home_making, name='home_making'),
    path('personal-care-assistant', views.personal_assistant,
         name='personal_assistant'),
    path('therapy', views.therapy, name='therapy'),
    path('iv-therapy', views.iv_therapy, name='iv_therapy'),
    path('interpretive-services', views.interpretive, name='interpretive'),
    path('independent-living-skills',
         views.independent_living, name='independent_living'),
    path('companion', views.companion, name='companion'),
    path('repite', views.respite, name='respite'),
    path('social-service', views.social_service, name='social_service'),
    path('hospice', views.hospice, name='hospice'),
]
