from selenium.webdriver.common.by import By
from description_of_elements import sauces_section, tab_sauces_section, fillings_section, tab_fillings_section, \
    buns_section, tab_buns_section


site = "https://stellarburgers.nomoreparties.site/"


def test_transition_sauces(start_browser):
    driver = start_browser
    driver.get(site)

    driver.find_element(By.XPATH, sauces_section).click()

    assert 'Соусы' == driver.find_element(By.CSS_SELECTOR, tab_sauces_section).text



def test_transition_fillings(start_browser):
    driver = start_browser
    driver.get(site)

    driver.find_element(By.XPATH, fillings_section).click()

    assert 'Начинки' == driver.find_element(By.CSS_SELECTOR, tab_fillings_section).text



def test_transition_buns(start_browser):
    driver = start_browser
    driver.get(site)

    driver.find_element(By.XPATH, fillings_section).click()
    driver.find_element(By.XPATH, buns_section).click()

    assert 'Булки' in driver.find_element(By.CSS_SELECTOR, tab_buns_section).text

