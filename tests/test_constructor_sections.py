from selenium import webdriver
from selenium.webdriver.common.by import By


def test_transition_personal_area_constructor(site):
    driver = webdriver.Chrome()
    driver.get(site)

    driver.find_element(By.XPATH, "//div[1]//nav/ul/li[1]/a/p").click()
    element_bottle = driver.find_element(By.XPATH, "//div[1]//main/section[1]/div[2]/ul[1]/a[1]/p")
    driver.execute_script("arguments[0].scrollIntoView();", element_bottle)

    assert 'Флюоресцентная булка R2-D3' == driver.find_element(By.XPATH,
                                                               "//div[1]//main/section[1]/div[2]/ul[1]/a[1]/p").text

    element_sause = driver.find_element(By.XPATH,
                                        "//div[1]/div/main/section[1]/div[2]/ul[2]/a[1]/p")
    driver.execute_script("arguments[0].scrollIntoView();", element_sause)

    assert 'Соус Spicy-X' == driver.find_element(By.XPATH,
                                                 "//div[1]/div/main/section[1]/div[2]/ul[2]/a[1]/p").text

    element_chop = driver.find_element(By.XPATH,
                                       "//div[1]//section[1]/div[2]/ul[3]/a[2]/p")
    driver.execute_script("arguments[0].scrollIntoView();", element_chop)

    assert 'Говяжий метеорит (отбивная)' == driver.find_element(By.XPATH,
                                                                "//div[1]//section[1]/div[2]/ul[3]/a[2]/p").text
