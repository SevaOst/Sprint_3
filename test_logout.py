from selenium.webdriver.chromium.webdriver import ChromiumDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

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
    # Кнопка Личный Кабинет на главной
    element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.LINK_TEXT, "Личный Кабинет")))
    element.click()
    # Кнопка Выход на странице профиля
    element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, ".//button[contains(text(), 'Выход')]")))
    element.click()
    # Кнопка Войти на странице логина
    assert driver.find_element(By.CLASS_NAME, "button_button__33qZ0").is_enabled()


