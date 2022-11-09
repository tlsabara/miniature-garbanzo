"""
App Users
"""
from django.contrib.auth import password_validation
from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _

# project imports
from core.models import GarbanzoPerms
from miniature_garbanzo.utils import functions
from miniature_garbanzo.utils.abcmodels import GarbanzoModel, CustomPermissionMixin

# local
from .managers import CustomUserManager
from .utils import AppUserChoices
from .validators import validador_cpf


class GarbanzoUser(GarbanzoModel, AbstractBaseUser, CustomPermissionMixin):
    # Campos obrigatórios
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # Campos não obrigatórios
    nome_completo_guser = models.CharField(max_length=255)
    dt_nasc_guser = models.DateField(blank=True, null=True)
    cpf_guser = models.CharField(max_length=11, validators=[validador_cpf])
    num_doc_guser = models.CharField(max_length=30, blank=True, null=True)
    genero_guser = models.CharField(
        max_length=30, choices=AppUserChoices.Commons.GENERO, blank=True, null=True
    )
    observacoes_guser = models.TextField(max_length=1000, blank=True, null=True)

    USERNAME_FIELD = "email"
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
            self.observacoes_guser = (
                f"{self.observacoes_guser}\n\n ---\n Nova Senha: {senha_nova}"
            )

        super().save(*args, **kwargs)
        if self._password is not None:
            password_validation.password_changed(self._password, self)
            self._password = None


class GUserPerms(GarbanzoModel):
    id_gperms = models.ForeignKey(GarbanzoPerms, on_delete=models.CASCADE)
    id_guser = models.ForeignKey(GarbanzoUser, on_delete=models.CASCADE)

    class Meta:
        db_table = "users_guserperms"
        unique_together = (("id_gperms", "id_guser"),)

    def __str__(self):
        return f"Permissao: {self.id_gperms} -> User: {self.id_guser}"


class Employee(GarbanzoModel):
    linked_user = models.OneToOneField(
        GarbanzoUser, on_delete=models.DO_NOTHING, editable=False
    )

    matricula_employee = models.CharField(max_length=10)
    rg_employee = models.CharField(max_length=10)
    full_name = models.CharField(max_length=10)
    dt_nasc = models.CharField(max_length=10)
    cargo = models.CharField(max_length=10)
    equipe = models.CharField(max_length=10)
    setor = models.CharField(max_length=10)
    gerente = models.CharField(max_length=10)
    centro_de_custo = models.CharField(max_length=10)
    dt_admissao = models.CharField(max_length=10)
    tipo_contrato = models.CharField(max_length=10)
    satus_contrato = models.CharField(max_length=10)
    empresa = models.CharField(max_length=10)
    unidade_empresa = models.CharField(max_length=10)
    status_operacional = models.CharField(max_length=10)
    op_vt = models.CharField(max_length=10)
    op_vr = models.CharField(max_length=10)
    tel_ctt_1 = models.CharField(max_length=10)
    tel_ctt_2 = models.CharField(max_length=10)
    email_pessoal = models.CharField(max_length=10)

    unique_together = (("linked_user", "matricula_employee"),)
