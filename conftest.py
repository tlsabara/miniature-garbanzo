import pytest
from django.contrib.auth import get_user_model
from assets.models import GarbanzoLinkType, GarbanzoAssetClass, GarbanzoAssetType


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
def fxt_new_extra_field_type(name=None, description=None, model=None):
    """
    Fixture para retornar os dados necessarios à criação de um novo ExtraFieldType
    """
    name = name if name else 'SSD'
    description = description if description else 'Unidade de armazenamento ssd'
    model = model if model else 'Computador'
    return {
        'name': name,
        'description': description,
        'model': model
    }


@pytest.fixture
def fxt_new_asset_item() -> dict:
    ...


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
