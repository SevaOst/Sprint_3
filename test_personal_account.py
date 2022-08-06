import time
from selenium.webdriver.chromium.webdriver import ChromiumDriver
from selenium.webdriver.common.by import By


def test_transition_to_personal_account_success(driver: ChromiumDriver):
    email = 'seva-ost1987@yandex.ru'
    # Кнопка Личный Кабинет на главной
    driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
    # Кнопка Email на странице логина
    driver.find_element(By.NAME, "name").send_keys(email)
    # Кнопка Пароль на странице логина
    driver.find_element(By.NAME, "Пароль").send_keys('qaqaqa')
    # Кнопка Войти на странице логина
    driver.find_element(By.CLASS_NAME, "button_button__33qZ0").click()
    time.sleep(1)
    # Кнопка Личный Кабинет на главной
    driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
    # Кнопка Профиль на странице профиля
    assert driver.find_element(By.LINK_TEXT, "Профиль").is_enabled()

def test_transition_from_personal_account_to_constructor_success(driver: ChromiumDriver):
    email = 'seva-ost1987@yandex.ru'
    # Кнопка Личный Кабинет на главной
    driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
    # Кнопка Email на странице логина
    driver.find_element(By.NAME, "name").send_keys(email)
    # Кнопка Пароль на странице логина
    driver.find_element(By.NAME, "Пароль").send_keys('qaqaqa')
    # Кнопка Войти на странице логина
    driver.find_element(By.CLASS_NAME, "button_button__33qZ0").click()
    time.sleep(1)
    # Кнопка Личный Кабинет на главной
    driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
    # Кнопка Конструктор на странице профиля
    driver.find_element(By.LINK_TEXT, "Конструктор").click()
    # Кнопка Оформить заказ на главной
    assert driver.find_element(By.XPATH, ".//button[contains(text(), 'Оформить заказ')]").is_enabled()

def test_transition_from_personal_account_to_main_success(driver: ChromiumDriver):
    email = 'seva-ost1987@yandex.ru'
    # Кнопка Личный Кабинет на главной
    driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
    # Кнопка Email на странице логина
    driver.find_element(By.NAME, "name").send_keys(email)
    # Кнопка Пароль на странице логина
    driver.find_element(By.NAME, "Пароль").send_keys('qaqaqa')
    # Кнопка Войти на странице логина
    driver.find_element(By.CLASS_NAME, "button_button__33qZ0").click()
    time.sleep(1)
    # Кнопка Личный Кабинет на главной
    driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
    # Логотип на странице профиля
    driver.find_element(By.XPATH, "/html/body/div/div/header/nav/div/a").click()
    # Кнопка Оформить заказ на главной
    assert driver.find_element(By.XPATH, ".//button[contains(text(), 'Оформить заказ')]").is_enabled()