from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_login_account_button_login_to_account(login, password, site):
    driver = webdriver.Chrome()
    driver.get(site)

    driver.find_element(By.XPATH, "//section[2]//button").click()
    driver.find_element(By.NAME, 'name').send_keys(login)
    driver.find_element(By.NAME, 'Пароль').send_keys(password)
    driver.find_element(By.XPATH, '//div[1]//button').click()
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable((By.XPATH, "//div[1]//section[2]//button")))

    assert "Оформить заказ" == driver.find_element(By.XPATH, "//div[1]//section[2]//button").text

    driver.quit()


def test_login_account_button_personal_area(login, password, site):
    driver = webdriver.Chrome()
    driver.get(site)

    driver.find_element(By.XPATH, "//div[1]//nav/a/p").click()
    driver.find_element(By.NAME, 'name').send_keys(login)
    driver.find_element(By.NAME, 'Пароль').send_keys(password)
    driver.find_element(By.XPATH, '//div[1]//button').click()
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable((By.XPATH, "//div[1]//section[2]//button")))

    assert "Оформить заказ" == driver.find_element(By.XPATH, "//div[1]//section[2]//button").text

    driver.quit()


def test_login_account_registration_form(login, password, site):
    driver = webdriver.Chrome()
    driver.get(site)

    driver.find_element(By.XPATH, "//section[2]//button").click()
    driver.find_element(By.XPATH, "//div[1]//p[1]/a").click()
    driver.find_element(By.XPATH, "//div[1]//p/a").click()
    driver.find_element(By.NAME, 'name').send_keys(login)
    driver.find_element(By.NAME, 'Пароль').send_keys(password)
    driver.find_element(By.XPATH, '//div[1]//button').click()
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable((By.XPATH, "//div[1]//section[2]//button")))

    assert "Оформить заказ" == driver.find_element(By.XPATH, "//div[1]//section[2]//button").text

    driver.quit()


def test_login_account_password_recovery_form(login, password, site):
    driver = webdriver.Chrome()
    driver.get(site)

    driver.find_element(By.XPATH, "//section[2]//button").click()
    driver.find_element(By.XPATH, "//div[1]//p[2]/a").click()
    driver.find_element(By.XPATH, "//div[1]//p/a").click()
    driver.find_element(By.NAME, 'name').send_keys(login)
    driver.find_element(By.NAME, 'Пароль').send_keys(password)
    driver.find_element(By.XPATH, '//div[1]//button').click()
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable((By.XPATH, "//div[1]//section[2]//button")))

    assert "Оформить заказ" == driver.find_element(By.XPATH, "//div[1]//section[2]//button").text

    driver.quit()
