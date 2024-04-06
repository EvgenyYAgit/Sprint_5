from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from description_of_elements import local_area_button, input_button, button_place_an_order, string_email_area_local, \
    string_password_area_local, constructor_button, logo


login = "krysenkov_7008@gmail.com"
password = "423567"
site = "https://stellarburgers.nomoreparties.site/"


def test_transition_personal_area_constructor(start_browser):
    driver = start_browser
    driver.get(site)

    driver.find_element(By.XPATH, local_area_button).click()
    driver.find_element(By.XPATH, string_email_area_local).send_keys(login)
    driver.find_element(By.XPATH, string_password_area_local).send_keys(password)
    driver.find_element(By.XPATH, input_button).click()
    driver.find_element(By.XPATH, local_area_button).click()
    driver.find_element(By.XPATH, constructor_button).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, button_place_an_order)))

    assert "Оформить заказ" == driver.find_element(By.XPATH, button_place_an_order).text



def test_transition_personal_area_logo(start_browser):
    driver = start_browser
    driver.get(site)

    driver.find_element(By.XPATH, local_area_button).click()
    driver.find_element(By.XPATH, string_email_area_local).send_keys(login)
    driver.find_element(By.XPATH, string_password_area_local).send_keys(password)
    driver.find_element(By.XPATH, input_button).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, button_place_an_order)))
    driver.find_element(By.XPATH, local_area_button).click()
    driver.find_element(By.CSS_SELECTOR, logo).click()

    assert "Оформить заказ" == driver.find_element(By.XPATH, button_place_an_order).text

