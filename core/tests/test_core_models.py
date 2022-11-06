import pytest
from core.models import GarbanzoPerms


@pytest.mark.django_db
def test_garbanzo_perms_model(fxt_new_perm_data) -> None:
    perm = GarbanzoPerms.objects.create(**fxt_new_perm_data)
    assert str(perm) == fxt_new_perm_data['sys_name_gperms']
    assert isinstance(perm, GarbanzoPerms)


@pytest.mark.django_db
def test_extra_field_type(fxt_new_link_type, fxt_new_asset_class, fxt_new_asset_type, fxt_new_extra_field_type) -> None:
    assert 1 == 2


def test_extra_field_model() -> None:
    assert 1 == 2
