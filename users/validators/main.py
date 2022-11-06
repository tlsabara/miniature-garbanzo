"""
Módulo para a validaçào de campos apenas para o APP USERS
"""
from django.core.exceptions import ValidationError

# local imports
from miniature_garbanzo.utils.validators import (
    validacao_apenas_numeros,
    validacao_onze_digitos,
)


def validador_cpf(val: str):
    validacao_apenas_numeros(val)
    validacao_onze_digitos(val)


if __name__ == "__main__":
    ...
