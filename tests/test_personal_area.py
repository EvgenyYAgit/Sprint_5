from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from description_of_elements import string_email_area_local, string_password_area_local, input_button, \
    button_place_an_order, local_area_button, profile_button


login = "krysenkov_7008@gmail.com"
password = "423567"
site = "https://stellarburgers.nomoreparties.site/"


def test_transition_personal_area(start_browser):
    driver = start_browser
    driver.get(site)

    driver.find_element(By.XPATH, local_area_button).click()
    driver.find_element(By.XPATH, string_email_area_local).send_keys(login)
    driver.find_element(By.XPATH, string_password_area_local).send_keys(password)
    driver.find_element(By.XPATH, input_button).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, button_place_an_order)))
    driver.find_element(By.XPATH, local_area_button).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, profile_button)))

    assert "Профиль" == driver.find_element(By.XPATH, profile_button).text
