import pytest
from django.contrib.auth.models import User
from payments.models import Wallet
from decimal import Decimal
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_new_transaction_api():
    client = APIClient()
    user = User.objects.create_user(username="user1", email="user1@test.com", password="pass")
    wallet = Wallet.objects.create(associated_user=user, company_name="Test", balance=Decimal("0.00"), payment_token="abc", wallet_address="addr123")
    
    data = {
        "amount": "50.00",
        "transaction_signature": "sig123",
        "user_wallet_address": "addr123"
    }

    response = client.post("/api/new_transaction/", data, format='json')
    assert response.status_code == 200
    assert "new_transaction_id" in response.data

@pytest.mark.django_db
def test_get_wallet_address_api():
    client = APIClient()
    user = User.objects.create_user(username="user2", password="pass")
    Wallet.objects.create(associated_user=user, company_name="Comp", balance=Decimal("0.00"), payment_token="tok456", wallet_address="wallet_xyz")

    response = client.get("/api/get_wallet_address/?payment_token=tok456")
    assert response.status_code == 200
    assert response.data["wallet_address"] == "wallet_xyz"
