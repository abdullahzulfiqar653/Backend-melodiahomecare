from django.shortcuts import render

from .models import Branch


def menu_branches(request):
    branches = Branch.objects.all()

    return {'branches': branches}
