from django import urls
from django.contrib.auth import get_user_model
import pytest

home_url = urls.reverse("home")
logout_url = urls.reverse("logoff_view")


# --------------------------------------------| Testes de Conectividade


@pytest.mark.parametrize(
    "param",
    [
        "home",
    ],
)
def test_render_opened_views(client, param) -> None:
    temp_url = urls.reverse(param)
    resp = client.get(temp_url)
    assert resp.status_code == 200


@pytest.mark.django_db
def test_user_login(client, fxt_create_test_user, fxt_new_user_data) -> None:
    user_model = get_user_model()
    assert user_model.objects.count() == 1
    resp = client.post(home_url, data=fxt_new_user_data)
    assert resp.status_code == 302
    assert resp.url == urls.reverse("my_home")


@pytest.mark.django_db
def test_user_logout(client, fxt_authenticated_user) -> None:
    resp = client.get(logout_url)
    assert resp.status_code == 302
    assert resp.url == urls.reverse("home")
