from django.urls import path, include

import core.views

urlpatterns = [
    path("", core.views.home, name="home"),
    path("myhome/", core.views.my_home, name="my_home"),
    path("logoff/", core.views.logoff_view, name="logoff_view"),
]
