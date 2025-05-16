import pytest
from django.contrib.auth.models import User
from payments.models import Wallet, Transaction
from decimal import Decimal

@pytest.mark.django_db
def test_wallet_str():
    user = User.objects.create_user(username="test", password="testpass")
    wallet = Wallet.objects.create(associated_user=user, company_name="TestCo", balance=Decimal("0.00"), payment_token="abc")
    assert str(wallet) == "TestCo's Wallet"

@pytest.mark.django_db
def test_transaction_str():
    user = User.objects.create_user(username="test2", email="test@test.com", password="testpass")
    tx = Transaction.objects.create(amount=Decimal("10.00"), associated_user=user, state="pending")
    assert "Transaction of 10.00 SOL to" in str(tx)

@pytest.mark.django_db
def test_wallet_negative_balance():
    user = User.objects.create_user(username="neg", password="testpass")
    with pytest.raises(ValueError):
        Wallet.objects.create(associated_user=user, company_name="NegCo", balance=Decimal("-1.00"), payment_token="def")

@pytest.mark.django_db
def test_transaction_zero_amount():
    user = User.objects.create_user(username="zero", password="testpass")
    with pytest.raises(ValueError):
        Transaction.objects.create(amount=Decimal("0.00"), associated_user=user)
