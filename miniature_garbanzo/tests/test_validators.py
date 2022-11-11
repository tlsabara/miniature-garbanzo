import pytest
from django.core.exceptions import ValidationError

from miniature_garbanzo.utils.validators import (
    validacao_apenas_numeros,
    validacao_onze_digitos,
)


@pytest.mark.parametrize("cpf_str", ["12345612341a"])
def test_validacaoapenasnumeros_raises_validation_error_if_value_not_is_digit(cpf_str):
    with pytest.raises(ValidationError):
        validacao_apenas_numeros(cpf_str)


@pytest.mark.parametrize("cpf_str", ["1231231231", "123123123123"])
def test_validacaoonzedigitos_raises_validation_error_if_len_not_is_exactly_11(cpf_str):
    with pytest.raises(ValidationError):
        validacao_onze_digitos(cpf_str)
