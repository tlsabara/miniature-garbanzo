from django.urls import path, include

import assets.views

urlpatterns = [
    path("", assets.views.assets_home, name="assets_home"),
]
