from django.urls import path, include

import users.views

urlpatterns = [
    path('', users.views.users_home, name='assets_home'),
]