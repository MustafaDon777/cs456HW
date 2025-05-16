import pytest
from django.urls import reverse
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_signup_view(client):
    response = client.get(reverse("signup"))
    assert response.status_code == 200
    assert "form" in response.context
