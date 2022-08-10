from selenium.webdriver.chromium.webdriver import ChromiumDriver
from selenium.webdriver.common.by import By


def test_constructor_sections_success():#driver: ChromiumDriver):
    # Кнопка Соусы на главной
    driver.find_element(By.XPATH, ".//section[1]/div[1]/div[2]/span").click()
    # Кнопка Начинки на главной
    driver.find_element(By.XPATH, ".//section[1]/div[1]/div[3]/span").click()
    # Кнопка Булки на главной
    driver.find_element(By.XPATH, ".//section[1]/div[1]/div[1]/span").click()

    assert driver.find_element(By.XPATH, ".//section[1]/div[2]/ul[2]/a[1]/p").is_displayed() \
           and driver.find_element(By.XPATH, ".//section[1]/div[2]/ul[1]/a[1]/p").is_displayed() \
           and driver.find_element(By.XPATH, ".//section[1]/div[2]/ul[3]/a[1]/p").is_displayed()
