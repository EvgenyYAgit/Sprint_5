import pytest
import random
from selenium import webdriver

@pytest.fixture
def new_email():
    new_email = f"krysenkov_7{random.randint(100, 999)}@gmail.com"
    return new_email

@pytest.fixture
def new_password():
    new_password = f'{random.randint(1000000, 9999999)}'
    return new_password

@pytest.fixture
def short_password():
    short_password = f'{random.randint(1000, 9999)}'
    return short_password

@pytest.fixture
def start_browser():
    start_browser = webdriver.Chrome()
    yield start_browser
    start_browser.quit()
