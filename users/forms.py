from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import CharField

from .models import GarbanzoUser


class GarbanzoUserCreationForm(UserCreationForm):
    class Meta:
        model = GarbanzoUser
        fields = ("email",)


class GarbanzoUserChangeForm(UserChangeForm):
    id = CharField()

    class Meta:
        model = GarbanzoUser
        fields = ("email",)
