"""
App Users
Neste modulo vou testar implementações

1 - Model de User customizado
2 - Utilização de UUID
3 - Utilização do HistoricalRecords()
"""
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords

# project imports
from miniature_garbanzo.utils.abcmodels import UUIDModel
from miniature_garbanzo.utils.validators import validacao_apenas_numeros, validacao_onze_digitos

# local
from .managers import CustomUserManager
from .utils import AppUserChoices


class GarbanzoUser(UUIDModel, AbstractBaseUser, PermissionsMixin):
    # Campos sistema
    system_create_at = models.DateTimeField(auto_now_add=True)
    system_edited_at = models.DateTimeField(auto_now=True)
    system_history = HistoricalRecords()

    # Campos obrigatórios
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    nome_completo_guser = models.CharField(max_length=255)
    dt_nasc_guser = models.DateField(blank=True, null=True)
    cpf_guser = models.CharField(max_length=11, validators=[validacao_apenas_numeros, validacao_onze_digitos])
    num_doc_guser = models.CharField(max_length=30, blank=True, null=True)
    genero_guser = models.CharField(max_length=30, choices=AppUserChoices.Commons.GENERO, blank=True, null=True)
    observacoes_guser = models.TextField(max_length=1000, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
