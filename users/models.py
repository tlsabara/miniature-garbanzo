"""
App Users
Neste modulo vou testar implementações

1 - Model de User customizado
2 - Utilização de UUID
3 - Utilização do HistoricalRecords()
"""
from django.contrib.auth import password_validation
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from miniature_garbanzo.utils import functions
# project imports
from miniature_garbanzo.utils.abcmodels import GarbanzoModel
from miniature_garbanzo.utils.validators import validacao_apenas_numeros, validacao_onze_digitos

# local
from .managers import CustomUserManager
from .utils import AppUserChoices
from .validators import validador_cpf


class GarbanzoUser(GarbanzoModel, AbstractBaseUser, PermissionsMixin):
    # Campos obrigatórios
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # Campos não obrigatórios
    nome_completo_guser = models.CharField(max_length=255)
    dt_nasc_guser = models.DateField(blank=True, null=True)
    cpf_guser = models.CharField(max_length=11, validators=[validador_cpf])
    num_doc_guser = models.CharField(max_length=30, blank=True, null=True)
    genero_guser = models.CharField(max_length=30, choices=AppUserChoices.Commons.GENERO, blank=True, null=True)
    observacoes_guser = models.TextField(max_length=1000, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        """
        Estou fazendo este override para grantir que o user será criado com uma senha randomica.
        :param args:
        :param kwargs:
        :return:
        """
        if self.password is None:
            senha_nova = functions.gerador_pwd(8)
            self.set_password(senha_nova)
            self.observacoes_guser = f'{self.observacoes_guser}\n\n ---\n Nova Senha: {senha_nova}'

        super().save(*args, **kwargs)
        if self._password is not None:
            password_validation.password_changed(self._password, self)
            self._password = None
