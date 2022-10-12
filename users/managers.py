from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

# project Imports
from miniature_garbanzo.utils import functions

class CustomUserManager(BaseUserManager):
    """
    Gerenciador para utilizar o email como login
    """
    def create_user(self, email, password, cpf_guser, nome_completo_user, **extra_fields):
        """
        Cria e salva o User com os dados informados
        """
        print(2)

        if not email:
            raise ValueError(_('O email deve ser configurado.'))

        if not password:
            senha_nova = functions.gerador_pwd(8)
            obs = extra_fields.get('observacoes_guser')
            obs = f'{obs}\n\n ---\n Nova Senha: {senha_nova}'
            extra_fields['observacoes_guser'] = obs

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.cpf_guser = cpf_guser
        user.nome_completo_user = nome_completo_user
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Cria um superusuário preenchido com os campos obrigatórios
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        nome_completo_guser = 'Garbanzo Admin'
        cpf_guser = '1111111111'

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser deve fazer parte do staff.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser deve ter permissão de Superuser.'))

        return self.create_user(email, password, cpf_guser, nome_completo_guser, **extra_fields)

