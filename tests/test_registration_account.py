import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_registration_account_new_random_login(site, password):
    driver = webdriver.Chrome()
    driver.get(site)

    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
    driver.find_element(By.XPATH, ".//a[text()='Зарегистрироваться']").click()
    new_title = f"krysenkov_7{random.randint(100, 999)}@gmail.com"
    driver.find_element(By.XPATH, ".//fieldset[1]//input").send_keys('Evgeny')
    driver.find_element(By.XPATH, ".//fieldset[2]//input").send_keys(new_title)
    driver.find_element(By.XPATH, ".//fieldset[3]//input").send_keys(password)
    driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()

    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable((By.XPATH, ".//a[text()='Зарегистрироваться']")))

    assert "Вход" == driver.find_element(By.XPATH, "//div[1]//h2").text

    driver.quit()


def test_registration_account_short_password(site):
    driver = webdriver.Chrome()
    driver.get(site)

    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
    driver.find_element(By.XPATH, ".//a[text()='Зарегистрироваться']").click()
    new_title = f"krysenkov_7{random.randint(100, 999)}@gmail.com"
    driver.find_element(By.XPATH, ".//fieldset[1]//input").send_keys('Evgeny')
    driver.find_element(By.XPATH, ".//fieldset[2]//input").send_keys(new_title)
    driver.find_element(By.XPATH, ".//fieldset[3]//input").send_keys("4235")
    driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//div[1]//fieldset[3]//p")))

    assert "Некорректный пароль" == driver.find_element(By.XPATH, "//div[1]//fieldset[3]//p").text

    driver.quit()
