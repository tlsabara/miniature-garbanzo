from datetime import datetime

import pytest
from django.contrib.auth import get_user_model
from assets.models import GarbanzoLinkType, GarbanzoAssetClass, GarbanzoAssetType, GarbanzoAssetItem
from core.models import ExtraFieldType


# -------------------------| Data Fixtures
@pytest.fixture
def fxt_new_user_data() -> dict:
    """
    Fixture para retornar os dados necessarios à criação de um novo Usuário
    """
    return {
        "email": "user_email",
        "cpf_guser": "12312312344",
        "password": "user_pass543",
        "nome_completo_guser": "Usuário Teste",
    }


@pytest.fixture
def fxt_new_user_data_full_without_staff(fxt_new_user_data) -> dict:
    """
    Fixture para retornar os dados necessarios à criação de um novo Usuário
    """
    fxt_new_user_data["genero_guser"] = 'masculino'
    fxt_new_user_data["num_doc_guser"] = "RG12123123"
    fxt_new_user_data["is_staff"] = False
    fxt_new_user_data["dt_nasc_guser"] = datetime(1990, 1, 1)
    return fxt_new_user_data


@pytest.fixture
def fxt_new_perm_data(desc_gperms=None, sys_name_gperms=None, long_desc_gperms=None, app_gperms=None) -> dict:
    """
    Fixture para retornar os dados necessarios à criação de uma nova GarbanzoPerms.
    """
    desc_gperms = desc_gperms if desc_gperms else 'Descrição da permissão'
    sys_name_gperms = sys_name_gperms if sys_name_gperms else 'CORE__segmento__tipo'
    long_desc_gperms = long_desc_gperms if long_desc_gperms else 'Descrição completa da permissaor'
    app_gperms = app_gperms if app_gperms else 'CORE'

    return {
        'desc_gperms': desc_gperms,
        'sys_name_gperms': sys_name_gperms,
        'long_desc_gperms': long_desc_gperms,
        'app_gperms': app_gperms
    }


@pytest.fixture
def fxt_new_link_type(value=None) -> dict:
    """
    Fixture para retornar os dados necessarios à criação de um novo GarbanzoLinkType.
    """
    value = value if value else 'asset_to_user'

    return {
        'desc_garbazno_link': value
    }


@pytest.fixture
def fxt_new_asset_class(accepted_links=None, desc_asset_class=None) -> dict:
    """
    Fixture para retornar os dados necessarios à criação de um novo GarbanzoAssetClass
    """
    accepted_links = accepted_links if accepted_links else ['asset_to_user']
    desc_asset_class = desc_asset_class if desc_asset_class else 'Asset Device'
    return {
        'desc_asset_class': desc_asset_class,
        'accepted_links': accepted_links
    }


@pytest.fixture
def fxt_new_asset_type(desc_asset_type=None, asset_type_class=None) -> dict:
    """
    Fixture para retornar os dados necessarios à criação de um novo GarbanzoAssetType
    """
    desc_asset_type = desc_asset_type if desc_asset_type else 'Computador'
    asset_type_class = asset_type_class if asset_type_class else 'Asset Device'
    return {
        'desc_asset_type': desc_asset_type,
        'asset_type_class': asset_type_class,
    }


@pytest.fixture
def fxt_new_asset_item(name_item=None, asset_number=None, serial_number=None, tag_number=None, type_asset=None) -> dict:
    """
    Fixture para retornar os dados necessarios à criação de um novo GarbanzoAssetItem
    """
    name_item = name_item if name_item else 'Computador0001'
    asset_number = asset_number if asset_number else 'COMPANY_A0001'
    serial_number = serial_number if serial_number else '43214321'
    tag_number = tag_number if tag_number else 'EVILCORP123MRBT'
    type_asset = type_asset if type_asset else 'Computador'
    return {
        'name_item': name_item,
        'asset_number': asset_number,
        'serial_number': serial_number,
        'tag_number': tag_number,
        'type_asset': type_asset
    }


@pytest.fixture
def fxt_new_extra_field_type(name=None, description=None, model=None, fixed_values=None) -> dict:
    """
    Retorna dadaos de texto para criação de um novo extra field type
    """
    name = name if name else 'SSD'
    description = description if description else 'Armazenamento de SSD'
    model = model if model else 'Computador'
    fixed_values = fixed_values if fixed_values else None

    return {
        'name': name,
        'description': description,
        'model': model,
        'fixed_values': fixed_values
    }


@pytest.fixture
def fxt_new_extra_field(item=None, field_type=None, value=None) -> dict:
    """
    Retorna o dicinario com os dados de texto para criar um novo extra field.
    """
    item = item if item else 'Computador0001'
    field_type = field_type if field_type else 'SSD'
    value = value if value else '120GB'

    return {
        'item': item,
        'field_type': field_type,
        'value': value
    }


# -------------------------| Functional Fixtures

# -------------------------| CORE
@pytest.fixture
def fxt_create_test_user(fxt_new_user_data) -> object:
    """
    Fixture para cirar um novo usuário
    """
    user_model = get_user_model()
    test_user = user_model.objects.create_user(**fxt_new_user_data)
    test_user.set_password(fxt_new_user_data.get("password"))
    return test_user


@pytest.fixture
def fxt_create_test_user_full_data(fxt_new_user_data_full_without_staff) -> object:
    """
    Fixture para cirar um novo usuário
    """
    user_model = get_user_model()
    test_user = user_model.objects.create_user(**fxt_new_user_data_full_without_staff)
    test_user.set_password(fxt_new_user_data_full_without_staff.get("password"))
    return test_user


@pytest.fixture
def fxt_authenticated_user(client, fxt_new_user_data) -> object:
    """
    Fixture para criar um cenário de usuário autenticado.
    """
    user_model = get_user_model()
    test_user = user_model.objects.create_user(**fxt_new_user_data)
    test_user.set_password(fxt_new_user_data.get("password"))
    test_user.save()
    client.login(**fxt_new_user_data)
    return test_user


# -------------------------| ASSETS
@pytest.fixture
@pytest.mark.parametrize(
    'value',
    [
        'asset_to_user',
        'asset_to_asset',
        'asset_to_location'
    ]
)
def fxt_create_garbanzolinktype(fxt_new_link_type) -> object:
    return GarbanzoLinkType.objects.create(**fxt_new_link_type)


@pytest.fixture
@pytest.mark.parametrize(
    'desc_asset_class, accepted_links',
    [
        ('Asset Device', ['asset_to_user', 'asset_to_location']),
        ('Asset Accessory', ['asset_to_asset', 'asset_to_location']),
    ]
)
def fxt_create_garbanzoassetclass(fxt_create_garbanzolinktype, fxt_new_asset_class) -> object:
    asset_class = GarbanzoAssetClass.objects.create()
    asset_class.desc_asset_class = fxt_new_asset_class['desc_asset_class']
    accepted_link_items = GarbanzoLinkType.objects.filter(desc_garbazno_link__in=fxt_new_asset_class['accepted_links'])
    asset_class.accepted_links.set(accepted_link_items)
    asset_class.save()
    return asset_class


@pytest.fixture
@pytest.mark.parametrize(
    'desc_asset_type, asset_type_class',
    [
        ('Computador', 'Asset Device'),
        ('Webcam', 'Asset Accessory')
    ]
)
def fxt_create_garbanzoassettype(fxt_create_garbanzoassetclass, fxt_new_asset_type) -> object:
    asset_type = GarbanzoAssetType.objects.create()
    asset_type.desc_asset_type = fxt_new_asset_type['desc_asset_type']
    asset_class = fxt_create_garbanzoassetclass
    asset_type.asset_type_class = asset_class
    asset_type.save()
    return asset_type


@pytest.fixture
def fxt_create_garbanzoassetitem(fxt_create_garbanzoassettype, fxt_new_asset_item):
    item = GarbanzoAssetItem.objects.create(
        type_asset=fxt_create_garbanzoassettype)
    item.asset_number = fxt_new_asset_item['asset_number']
    item.name_item = fxt_new_asset_item['name_item']
    item.serial_number = fxt_new_asset_item['serial_number']
    item.tag_number = fxt_new_asset_item['tag_number']
    item.save()
    return item


@pytest.fixture
def fxt_create_extrafieldtype(fxt_create_garbanzoassettype, fxt_new_extra_field_type) -> object:
    extra_field_type = ExtraFieldType.objects.create(model=fxt_create_garbanzoassettype)
    extra_field_type.name = fxt_new_extra_field_type['name']
    extra_field_type.description = fxt_new_extra_field_type['description']
    extra_field_type.save()
    return extra_field_type
