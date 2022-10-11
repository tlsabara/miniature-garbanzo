from django.contrib.auth.base_user import BaseUserManager
from datetime import datetime

# Removido >> from django.utils.translation import ugettext_lazy as _
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Gerenciador para utilizar o email como login
    """
    def create_user(self, email, password, **extra_fields):
        """
        Cria e salva o User com os dados informados
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Cria um superusuário
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('nome_completo_guser', 'Garbanzo Admin')
        extra_fields.setdefault('cpf_guser', '999999999')
        extra_fields.setdefault('num_doc_guser', 'Não informado')
        extra_fields.setdefault('nome_completo_guser', 'Garbanzo Admin')
        extra_fields.setdefault('dt_nasc_guser', datetime.fromisoformat('1992-06-02'))

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser deve fazer parte do staff.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser deve ter permissão de Superuser.'))

        return self.create_user(email, password, **extra_fields)
