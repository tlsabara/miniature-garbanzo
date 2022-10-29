from django.http import Http404
from django.shortcuts import render

# Create your views here.
def assets_home(request):
    return Http404