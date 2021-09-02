from career.models import Branch
from django.shortcuts import get_object_or_404, render
from .models import *
# Create your views here.


def branch(request, slug):
    branchs = Branch.objects.filter(slug=slug).first()
    # branchs = get_object_or_404(Branch, slug=slug)
    return render(request, 'branches.html', {'branches': branchs})
