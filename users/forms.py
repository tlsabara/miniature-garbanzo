from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import GarbanzoUser


class GarbanzoUserCreationForm(UserCreationForm):

    class Meta:
        model = GarbanzoUser
        fields = ('email',)


class GarbanzoUserChangeForm(UserChangeForm):

    class Meta:
        model = GarbanzoUser
        fields = ('email',)
