from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# project imports
from miniature_garbanzo.utils.abcmodels import UUIDModel
from miniature_garbanzo.utils.validators import validacao_apenas_numeros, validacao_onze_digitos

# local
from .managers import CustomUserManager

"""
Neste modulo vou testar implementações

1 - Model de User customizado
2 - Utilização de UUID 
"""


class GarbanzoUser(UUIDModel, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # mudar esse date_joined
    date_joined = models.DateTimeField(default=timezone.now)
    nome_completo_guser = models.CharField(max_length=255)
    dt_nasc_guser = models.DateField()
    cpf_guser = models.CharField(max_length=11, validators=[validacao_apenas_numeros, validacao_onze_digitos])
    num_doc_guser = models.CharField(max_length=30)
    cargo_guser = models.CharField(max_length=100, blank=True, null=True)
    setor_guser = models.CharField(max_length=100, blank=True, null=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
