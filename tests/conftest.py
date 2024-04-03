import pytest

@pytest.fixture
def login():
    login = "krysenkov_7008@gmail.com"
    return login

@pytest.fixture
def password():
    password = "423567"
    return password

@pytest.fixture
def site():
    site = "https://stellarburgers.nomoreparties.site/"
    return site
