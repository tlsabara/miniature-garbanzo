from django.http import Http404, HttpResponse
from django.shortcuts import render

# Create your views here.
def assets_home(request):
    return HttpResponse(content="Not Found", status=404)
