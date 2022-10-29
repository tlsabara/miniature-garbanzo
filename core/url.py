from django.urls import path, include

import core.views

urlpatterns = [
    path('', core.views.home, name='home' ),
]
