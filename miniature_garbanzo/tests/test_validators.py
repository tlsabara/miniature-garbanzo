import pytest
from django.core.exceptions import ValidationError

from miniature_garbanzo.utils.validators import validacao_apenas_numeros


@pytest.mark.parametrize("cpf_str", ["12345612341a"])
def test_validacaoapenasnumeros_raises_validation_error_if_value_not_is_digit(cpf_str):
    with pytest.raises(ValidationError):
        validacao_apenas_numeros(cpf_str)
