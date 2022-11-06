import pytest

from assets.models import GarbanzoLinkType, GarbanzoAssetClass, GarbanzoAssetType


@pytest.mark.django_db
def test_garbanzolinktype_model(fxt_new_link_type) -> None:
    link_type = GarbanzoLinkType.objects.create(**fxt_new_link_type)
    assert str(link_type) == fxt_new_link_type['desc_garbazno_link']
    assert isinstance(link_type, GarbanzoLinkType)


@pytest.mark.django_db
def test_garbanzoassetclass_model(fxt_create_garbanzolinktype, fxt_new_asset_class):
    asset_class = GarbanzoAssetClass.objects.create()
    asset_class.desc_asset_class = fxt_new_asset_class['desc_asset_class']
    accepted_link_items = GarbanzoLinkType.objects.filter(desc_garbazno_link=fxt_new_asset_class['accepted_links'])
    asset_class.accepted_links.set(accepted_link_items)
    asset_class.save()
    assert GarbanzoAssetClass.objects.count() == 1
    assert str(asset_class) == fxt_new_asset_class['desc_asset_class']
    assert isinstance(asset_class, GarbanzoAssetClass)


@pytest.mark.django_db
def test_garbanzoassettype_model(fxt_create_garbanzoassetclass, fxt_new_asset_type) -> None:

    asset_type = GarbanzoAssetType.objects.create()
    asset_type.desc_asset_type = fxt_new_asset_type['desc_asset_type']
    asset_type.asset_type_class = GarbanzoAssetClass.objects.filter(desc_asset_class__exact=['asset_type_class'])
    assert GarbanzoAssetType.objects.count() == 1
    assert str(asset_type) == fxt_new_asset_type['desc_asset_type']
    assert isinstance(asset_type, GarbanzoAssetType)
