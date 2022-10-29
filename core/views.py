from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template import loader

from miniature_garbanzo.settings import STATICFILES_DIRS


# Create your views here.
def home(request):
    print(STATICFILES_DIRS)
    return render(request, 'core/login-register.html')

