from django import urls
from django.contrib.auth import get_user_model
import pytest

home_url = urls.reverse("home")
logout_url = urls.reverse('logoff_view')


# --------------------------------------------| Testes de Conectividade

@pytest.mark.parametrize('param', [
    ('home'),
])
def test_render_opened_views(client, param):
    temp_url = urls.reverse(param)
    resp = client.get(temp_url)
    assert resp.status_code == 200


@pytest.mark.django_db
def test_user_login(client, create_test_user, user_data):
    user_model = get_user_model()
    assert user_model.objects.count() == 1
    resp = client.post(home_url, data=user_data)
    assert resp.status_code == 302
    assert resp.url == urls.reverse('my_home')


@pytest.mark.django_db
def test_user_logout(client, authenticated_user):
    resp = client.get(logout_url)
    assert resp.status_code == 302
    assert resp.url == urls.reverse('home')
