import pytest


@pytest.mark.django_db
def test_create_simple_user(fxt_create_test_user, fxt_new_user_data) -> None:
    assert str(fxt_create_test_user) == fxt_new_user_data['email']
    assert fxt_create_test_user.nome_completo_guser == fxt_new_user_data['nome_completo_guser']


@pytest.mark.django_db
def test_create_user_with_full_data(fxt_create_test_user_full_data, fxt_new_user_data_full_without_staff) -> None:
    assert str(fxt_create_test_user_full_data) == fxt_new_user_data_full_without_staff['email']
    assert fxt_create_test_user_full_data.email == fxt_new_user_data_full_without_staff['email']
    assert fxt_create_test_user_full_data.nome_completo_guser == fxt_new_user_data_full_without_staff['nome_completo_guser']
    assert fxt_create_test_user_full_data.num_doc_guser == fxt_new_user_data_full_without_staff['num_doc_guser']
    assert fxt_create_test_user_full_data.genero_guser == fxt_new_user_data_full_without_staff['genero_guser']
    assert fxt_create_test_user_full_data.dt_nasc_guser == fxt_new_user_data_full_without_staff['dt_nasc_guser']
    assert fxt_create_test_user_full_data.is_staff == fxt_new_user_data_full_without_staff['is_staff']
