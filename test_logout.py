import time
from selenium.webdriver.chromium.webdriver import ChromiumDriver
from selenium.webdriver.common.by import By

def test_logout_success(driver: ChromiumDriver):
    email = 'seva-ost1987@yandex.ru'
    # Кнопка входа на главной
    driver.find_element(By.XPATH, ".//div/button[text()='Войти в аккаунт']").click()
    # Кнопка Email на странице логина
    driver.find_element(By.NAME, "name").send_keys(email)
    # Кнопка Пароль на странице логина
    driver.find_element(By.NAME, "Пароль").send_keys('qaqaqa')
    # Кнопка Войти на странице логина
    driver.find_element(By.CLASS_NAME, "button_button__33qZ0").click()
    time.sleep(1)
    # Кнопка Личный Кабинет на главной
    driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
    # Кнопка Выход на странице профиля
    driver.find_element(By.LINK_TEXT, "Выход").click()
    # Кнопка Войти на странице логина
    assert driver.find_element(By.CLASS_NAME, "button_button__33qZ0").is_enabled()


