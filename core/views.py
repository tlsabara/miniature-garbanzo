from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from core.froms import UserLoginForm
from users.models import GUserPerms


# Create your views here.
def home(request):
    form = UserLoginForm
    if request.method == "GET":
        if request.user.is_anonymous:
            context = "Anônimo"
            return render(
                request,
                "core/login-register.html",
                {
                    "user": request.user,
                    "form": form,
                    "context": context,
                },
            )
        else:
            return redirect("my_home")
    elif request.method == "POST":
        username = request.POST.get("email", "")
        password = request.POST.get("password", "")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("my_home")
        else:
            context = {"error": "Wrong credintials"}
            return render(
                request,
                "core/login-register.html",
                {
                    "context": context,
                    "user": request.user,
                    "perms": [],
                },
            )


def my_home(request):
    context = "logado"
    if request.user.is_authenticated:
        permissao = (
            GUserPerms.objects.filter(id_guser=request.user)
            if not request.user.is_anonymous
            else []
        )
        return render(
            request,
            "core/home.html",
            {
                "user": request.user,
                # to-do  reflete nisso aqui, to usando na home, mas deve ser usado no menu tmb.
                "perms": permissao,
                "context": context,
            },
        )
    else:
        return Http404


def logoff_view(request):
    logout(request)
    return redirect("home")
