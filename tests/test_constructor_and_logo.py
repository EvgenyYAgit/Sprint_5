from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_transition_personal_area_constructor(login, password, site):
    driver = webdriver.Chrome()
    driver.get(site)

    driver.find_element(By.XPATH, "//div[1]//nav/a/p").click()
    driver.find_element(By.NAME, 'name').send_keys(login)
    driver.find_element(By.NAME, 'Пароль').send_keys(password)
    driver.find_element(By.XPATH, '//div[1]//button').click()
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable((By.XPATH, "//div[1]//section[2]//button")))
    driver.find_element(By.XPATH, "//div[1]//nav/a/p").click()
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable((By.XPATH, "//div[1]//nav/p")))
    driver.find_element(By.XPATH, "//div[1]//nav/ul/li[1]/a/p").click()

    assert "Оформить заказ" == driver.find_element(By.XPATH, "//div[1]//section[2]//button").text
    driver.quit()


def test_transition_personal_area_logo(login, password, site):
    driver = webdriver.Chrome()
    driver.get(site)

    driver.find_element(By.XPATH, "//div[1]//nav/a/p").click()
    driver.find_element(By.NAME, 'name').send_keys(login)
    driver.find_element(By.NAME, 'Пароль').send_keys(password)
    driver.find_element(By.XPATH, '//div[1]//button').click()
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable((By.XPATH, "//div[1]//section[2]//button")))
    driver.find_element(By.XPATH, "//div[1]//nav/a/p").click()
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable((By.XPATH, "//div[1]//nav/p")))
    driver.find_element(By.CSS_SELECTOR, "[xmlns='http://www.w3.org/2000/svg'][width='290']").click()

    assert "Оформить заказ" == driver.find_element(By.XPATH, "//div[1]//section[2]//button").text
    driver.quit()
