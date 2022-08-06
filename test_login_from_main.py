import time
from selenium.webdriver.chromium.webdriver import ChromiumDriver
from selenium.webdriver.common.by import By

def test_login_account_button_from_main_success(driver: ChromiumDriver):
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
    # Кнопка Оформить заказ на главной
    assert driver.find_element(By.XPATH, ".//button[contains(text(), 'Оформить заказ')]").is_enabled()

def test_login_personal_account_success(driver: ChromiumDriver):
    email = 'seva-ost1987@yandex.ru'
    # Кнопка Личный Кабинет на главной
    driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
    # Кнопка Email на странице логина
    driver.find_element(By.NAME, "name").send_keys(email)
    # Кнопка Пароль на странице логина
    driver.find_element(By.NAME, "Пароль").send_keys('qaqaqa')
    # Кнопка Войти на странице логина
    driver.find_element(By.CLASS_NAME, "button_button__33qZ0").click()
    # Кнопка Оформить заказ на главной
    assert driver.find_element(By.XPATH, ".//button[contains(text(), 'Оформить заказ')]").is_enabled()

def test_login_from_registration_success(driver: ChromiumDriver):
    email = 'seva-ost1987@yandex.ru'
    # Кнопка входа на главной
    driver.find_element(By.XPATH, ".//div/button[text()='Войти в аккаунт']").click()
    # Ссылка 'Зарегистрироваться' на странице логина
    driver.find_element(By.LINK_TEXT, 'Зарегистрироваться').click()
    # Ссылка 'Войти' на странице регистрации
    driver.find_element(By.LINK_TEXT, 'Войти').click()
    # Кнопка Email на странице логина
    driver.find_element(By.NAME, "name").send_keys(email)
    # Кнопка Пароль на странице логина
    driver.find_element(By.NAME, "Пароль").send_keys('qaqaqa')
    # Кнопка Войти на странице логина
    driver.find_element(By.CLASS_NAME, "button_button__33qZ0").click()
    # Кнопка Оформить заказ на главной
    assert driver.find_element(By.XPATH, ".//button[contains(text(), 'Оформить заказ')]").is_enabled()

def test_login_from_password_recovery_success(driver: ChromiumDriver):
    email = 'seva-ost1987@yandex.ru'
    # Кнопка входа на главной
    driver.find_element(By.XPATH, ".//div/button[text()='Войти в аккаунт']").click()
    # Ссылка 'Восстановить пароль' на странице логина
    driver.find_element(By.LINK_TEXT, 'Восстановить пароль').click()
    # Ссылка 'Войти' на странице восстановления пароля
    driver.find_element(By.LINK_TEXT, 'Войти').click()
    # Кнопка Email на странице логина
    driver.find_element(By.NAME, "name").send_keys(email)
    # Кнопка Пароль на странице логина
    driver.find_element(By.NAME, "Пароль").send_keys('qaqaqa')
    # Кнопка Войти на странице логина
    driver.find_element(By.CLASS_NAME, "button_button__33qZ0").click()
    time.sleep(2)
    # Кнопка Оформить заказ на главной
    assert driver.find_element(By.XPATH, ".//button[contains(text(), 'Оформить заказ')]").is_enabled()






