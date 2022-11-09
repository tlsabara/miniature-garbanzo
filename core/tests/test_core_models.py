import pytest
from core.models import GarbanzoPerms, ExtraFieldType, ExtraField


@pytest.mark.django_db
def test_garbanzo_perms_model(fxt_new_perm_data) -> None:
    perm = GarbanzoPerms.objects.create(**fxt_new_perm_data)
    assert GarbanzoPerms.objects.count() == 1
    assert str(perm) == fxt_new_perm_data["sys_name_gperms"]
    assert isinstance(perm, GarbanzoPerms)


@pytest.mark.django_db
def test_extra_field_type_without_field_fixedvalues(
    fxt_create_garbanzoassettype, fxt_new_extra_field_type
) -> None:
    extra_field_type = ExtraFieldType.objects.create(model=fxt_create_garbanzoassettype)
    extra_field_type.name = fxt_new_extra_field_type["name"]
    extra_field_type.description = fxt_new_extra_field_type["description"]
    extra_field_type.save()
    assert ExtraFieldType.objects.count() == 1
    assert str(extra_field_type) == fxt_new_extra_field_type["name"]
    assert isinstance(extra_field_type, ExtraFieldType)


@pytest.mark.django_db
def test_extra_field_model(
    fxt_create_garbanzoassetitem, fxt_create_extrafieldtype, fxt_new_extra_field
) -> None:
    extra_field = ExtraField.objects.create(
        item=fxt_create_garbanzoassetitem,
        field_type=fxt_create_extrafieldtype,
        value=fxt_new_extra_field["value"],
    )
    extra_field.save()
    assert ExtraField.objects.count() == 1
    assert (
        str(extra_field)
        == f"{str(fxt_create_extrafieldtype)} on ASSET: {fxt_create_garbanzoassetitem.asset_number}"
    )
    assert extra_field.item.id == fxt_create_garbanzoassetitem.id
    assert isinstance(extra_field, ExtraField)
