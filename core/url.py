from django.urls import path, include

import core.views

urlpatterns = [
    path('', core.views.home, name='home' ),
    path('logoff/', core.views.logoff_view, name='logoff_view'),
]
