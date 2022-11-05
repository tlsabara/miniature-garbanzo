from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.contrib.auth import authenticate, login, logout

from core.froms import UserLoginForm
from miniature_garbanzo.settings import STATICFILES_DIRS
from users.models import GUserPerms


# Create your views here.
def home(request):
    print(STATICFILES_DIRS)
    # to-do Isso aqui precisa ser melhorado.
    permissao = GUserPerms.objects.filter(id_guser=request.user) if not request.user.is_anonymous else []
    # ---
    form = UserLoginForm
    if request.method == 'GET':
        if request.user.is_anonymous:
            context = 'Anonimo'
            return render(request, 'core/login-register.html',
                          {
                              'user': request.user,
                              'form': form,
                              'context': context,
                          }
                      )
        else:
            context = 'logado'
            return render(request, 'core/home.html',
                          {
                              'user': request.user,
                              'form': form,
                              # to-do  reflete nisso aqui, to usando na home, mas deve ser usado no menu tmb.
                              'perms': permissao,
                              'context': context,
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
            context = 'tentando login'
            return redirect('home')
        else:
            context = {'error': 'Wrong credintials'}  # to display error?
            return render(request, 'core/login-register.html', {
                'context': context,
                'user': request.user,
                'perms': permissao # to-do ta começando a cagar no projeto

            })


def logoff_view(request):
    logout(request)
    return redirect('home')

