from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from description_of_elements import login_button, string_email_area_local, string_password_area_local, input_button, \
    button_place_an_order, local_area_button, register_button_string, input_button_registration, \
    recovery_password_button


login = "krysenkov_7008@gmail.com"
password = "423567"
site = "https://stellarburgers.nomoreparties.site/"


def test_login_account_button_login_to_account(start_browser):
    driver = start_browser
    driver.get(site)

    driver.find_element(By.XPATH, login_button).click()
    driver.find_element(By.XPATH, string_email_area_local).send_keys(login)
    driver.find_element(By.XPATH, string_password_area_local).send_keys(password)
    driver.find_element(By.XPATH, input_button).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, button_place_an_order)))

    assert "Оформить заказ" == driver.find_element(By.XPATH, button_place_an_order).text



def test_login_account_button_personal_area(start_browser):
    driver = start_browser
    driver.get(site)

    driver.find_element(By.XPATH, local_area_button).click()
    driver.find_element(By.XPATH, string_email_area_local).send_keys(login)
    driver.find_element(By.XPATH, string_password_area_local).send_keys(password)
    driver.find_element(By.XPATH, input_button).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, button_place_an_order)))

    assert "Оформить заказ" == driver.find_element(By.XPATH, button_place_an_order).text



def test_login_account_registration_form(start_browser):
    driver = start_browser
    driver.get(site)

    driver.find_element(By.XPATH, login_button).click()
    driver.find_element(By.XPATH, register_button_string).click()
    driver.find_element(By.XPATH, input_button_registration).click()
    driver.find_element(By.XPATH, string_email_area_local).send_keys(login)
    driver.find_element(By.XPATH, string_password_area_local).send_keys(password)
    driver.find_element(By.XPATH, input_button).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, button_place_an_order)))

    assert "Оформить заказ" == driver.find_element(By.XPATH, button_place_an_order).text



def test_login_account_password_recovery_form(start_browser):
    driver = start_browser
    driver.get(site)

    driver.find_element(By.XPATH, login_button).click()
    driver.find_element(By.XPATH, recovery_password_button).click()
    driver.find_element(By.XPATH, input_button_registration).click()
    driver.find_element(By.XPATH, string_email_area_local).send_keys(login)
    driver.find_element(By.XPATH, string_password_area_local).send_keys(password)
    driver.find_element(By.XPATH, input_button).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, button_place_an_order)))

    assert "Оформить заказ" == driver.find_element(By.XPATH, button_place_an_order).text

