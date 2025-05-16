import pytest
from payments.forms import add_user_and_wallet
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_add_user_and_wallet_form_valid():
    form_data = {
        'username': 'testuser',
        'email': 'testuser@test.com',
        'password1': 'Password123!',
        'password2': 'Password123!',
        'company_name': 'Test Company',
        'payment_token': 'testtoken123'
    }
    form = add_user_and_wallet(data=form_data)
    assert form.is_valid()
    user = form.save()
    assert user.username == 'testuser'
    assert user.wallet.company_name == 'Test Company'
