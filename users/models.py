"""
App Users
Neste modulo vou testar implementações

1 - Model de User customizado
2 - Utilização de UUID
3 - Utilização do HistoricalRecords()
"""
from django.contrib.auth import password_validation
from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords

from miniature_garbanzo.utils import functions
# project imports
from miniature_garbanzo.utils.abcmodels import GarbanzoModel, CustomPermissionMixin

# local
from .managers import CustomUserManager
from .utils import AppUserChoices
from .validators import validador_cpf




class GarbanzoUser(GarbanzoModel, AbstractBaseUser, CustomPermissionMixin):
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


class GarbanzoPerms(GarbanzoModel):
    desc_gperms = models.CharField(max_length=100)
    sys_name_gperms = models.CharField(max_length=100)
    long_desc_gperms = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.sys_name_gperms


class GUserPerms(GarbanzoModel):
    id_gperms = models.ForeignKey(GarbanzoPerms, on_delete=models.CASCADE)
    id_guser = models.ForeignKey(GarbanzoUser, on_delete=models.CASCADE)

    class Meta:
        # managed = False
        db_table = 'users_guserperms'
        unique_together = (('id_gperms', 'id_guser'),)

    def __str__(self):
        return f'Permissao: {self.id_gperms} -> User: {self.id_guser}'


class GarbanzoLinkType(GarbanzoModel):
    desc_garbazno_link = models.CharField(max_length=100)

    def __str__(self):
        return self.desc_garbazno_link


class GarbanzoAssetType(GarbanzoModel):
    desc_asset_type = models.CharField(max_length=100)
    accepted_links = models.ManyToManyField(GarbanzoLinkType,)

    def __str__(self):
        return self.desc_asset_type


class GarbanzoAssetItem(GarbanzoModel):
    name_item = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    tag_number = models.CharField(max_length=100)
    internal_number = models.CharField(max_length=100)
    type_asset = models.ForeignKey(GarbanzoAssetType, on_delete= models.DO_NOTHING)

    def __str__(self):
        return f'{self.name_item} - ({self.internal_number}) - ({self.type_asset})'


class TesteId(models.Model):
    id = models.CharField(max_length=10)
    nome = models.CharField(max_length=10, primary_key=True)
    history = HistoricalRecords()


class TesteFkId(models.Model):
    teste = models.ForeignKey(TesteId, on_delete=models.DO_NOTHING)
    history = HistoricalRecords()
