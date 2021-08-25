from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Blog
# Create your views here.


def home(request):
    blog = Blog.objects.all()
    return render(request, 'index.html', {'blog': blog})
