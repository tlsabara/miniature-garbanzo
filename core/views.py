from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.contrib.auth import authenticate, login

from core.froms import UserLoginForm
from miniature_garbanzo.settings import STATICFILES_DIRS


# Create your views here.
def home(request):
    print(STATICFILES_DIRS)
    form = UserLoginForm

    if request.method == 'GET':
        context = ''
        return render(request, 'core/login-register.html',
                      {
                          'user': request.user,
                          'form': form
                      }
                      )
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page?
            # return HttpResponseRedirect('/')
            context = ''
            return render(request, 'core/home.html', {'context': context, 'user': request.user})
        else:
            context = {'error': 'Wrong credintials'}  # to display error?
            return render(request, 'core/home.html', {'context': context, 'user': request.user})



