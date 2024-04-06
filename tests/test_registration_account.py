from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from description_of_elements import login_button, register_button_string, register_button, input_button, string_name, \
    string_email, string_password, error_line_incorrect_password

site = "https://stellarburgers.nomoreparties.site/"


def test_registration_account_new_random_login(start_browser, new_email, new_password):
    driver = start_browser
    driver.get(site)

    driver.find_element(By.XPATH, login_button).click()
    driver.find_element(By.XPATH, register_button_string).click()
    driver.find_element(By.XPATH, string_name).send_keys('Evgeny')
    driver.find_element(By.XPATH, string_email).send_keys(new_email)
    driver.find_element(By.XPATH, string_password).send_keys(new_password)
    driver.find_element(By.XPATH, register_button).click()

    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, register_button_string)))

    assert "Войти" == driver.find_element(By.XPATH, input_button).text


def test_registration_account_short_password(start_browser, new_email, short_password):
    driver = start_browser
    driver.get(site)

    driver.find_element(By.XPATH, login_button).click()
    driver.find_element(By.XPATH, register_button_string).click()
    driver.find_element(By.XPATH, string_name).send_keys('Evgeny')
    driver.find_element(By.XPATH, string_email).send_keys(new_email)
    driver.find_element(By.XPATH, string_password).send_keys(short_password)
    driver.find_element(By.XPATH, register_button).click()

    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, error_line_incorrect_password)))

    assert "Некорректный пароль" == driver.find_element(By.XPATH, error_line_incorrect_password).text
