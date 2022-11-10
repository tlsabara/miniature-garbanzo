import pytest
from django import urls


assets_home_url = urls.reverse("assets_home")


@pytest.mark.django_db
def test_view_assetshome_returns_404(fxt_authenticated_user, client):
    resp = client.get(assets_home_url)
    assert resp.status_code == 404
