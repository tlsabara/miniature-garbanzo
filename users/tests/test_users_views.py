import pytest
from django import urls

users_home_url = urls.reverse("users_home")


@pytest.mark.django_db
def test_view_usershome_returns_404(fxt_authenticated_user, client):
    resp = client.get(users_home_url)
    assert resp.status_code == 404
