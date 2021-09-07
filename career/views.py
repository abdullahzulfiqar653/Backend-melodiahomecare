from career.models import Branch
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from .forms import ApplyForm
# Create your views here.


def branch(request, slug):
    branches = Branch.objects.filter(slug=slug)
    branches = branches.first()
    # branchs = get_object_or_404(Branch, slug=slug)
    return render(request, 'branches.html', {'branches': branches})


def benefits(request):
    benfts = Employee_Benefits.objects.all()
    return render(request, 'employee-benefits.html', {'benefits': benfts})


def job_opening(request):
    job = Job_Opening.objects.all()
    return render(request, 'job-opening.html', {'jobs': job})


def areas(request):
    area = Areas.objects.all()
    return render(request, 'services-and-areas.html', {'area': area})


def team(request):
    teams = Team.objects.all()
    return render(request, 'about.html', {'team': teams})


def apply_now(request):
    if request.method=='POST':
        form = ApplyForm(request.POST, request.FILES)
        print(form)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect("/")
    form = ApplyForm()
    return render(request, "apply-now.html", {'form': form})
