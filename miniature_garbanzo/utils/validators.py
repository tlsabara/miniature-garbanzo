"""
Módulo para a validaçào de campos
"""
from django.core.exceptions import ValidationError


def validacao_apenas_numeros(val: str):
    """
    Valida se o valor no campo contem apenas numeros.
        Utilize em validação de campos Charfield que devem aceitar apenas numeros.
    :param val: Valor a ser inserido no campo.
    :return:
    """
    if not val.isdigit():
        raise ValidationError("Este campo deve ter apenas numeros")


def validacao_onze_digitos(val: str):
    """
    Valida se val tem 11 digitos.
        Utilizada em validação de CPF.
    :param val: Valor a ser inserido no campo.
    :return:
    """
    if not len(val) == 11:
        raise ValidationError("Este campo deve ter exatamente 11 digitos.")


if __name__ == "__main__":
    ...
