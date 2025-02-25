import pytest
from main import BankAccount

@pytest.fixture
def bank_account():
    return BankAccount("Test User", 1000)

def test_deposit(bank_account):
    assert bank_account.deposit(500) == "Deposited 500. New balance: 1500"
    assert bank_account.deposit(-100) == "Invalid deposit amount."

def test_withdraw(bank_account):
    assert bank_account.withdraw(300) == "Withdrew 300. New balance: 700"
    assert bank_account.withdraw(2000) == "Invalid withdrawal amount or insufficient funds."

def test_get_balance(bank_account):
    assert bank_account.get_balance() == "Current balance: 1000"
