import time
from selenium.webdriver.chromium.webdriver import ChromiumDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def test_success_registration(driver: ChromiumDriver):
    email = 'seva' + str(time.time()) + '@yandex.ru'
    # Кнопка входа на главной
    driver.find_element(By.XPATH, ".//div/button[text()='Войти в аккаунт']").click()
    # Ссылка 'Зарегистрироваться' на странице логина
    driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()
    # Поле Имя на странице регистрации
    driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys('Seva')
    assert driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input[@value = 'Seva']")
    # Поле Email на странице регистрации
    driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys(email)
    # Поле Пароль на странице регистрации
    driver.find_element(By.XPATH, ".//fieldset[3]/div/div/input").send_keys('qaqaqa')
    # Ссылка 'Зарегистрироваться' на странице регистрации
    driver.find_element(By.XPATH, ".//form/button[text()='Зарегистрироваться']").click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, ".//form/button[text()='Войти']")))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login', "Не перешли на стартовую страницу"
    print("Перешли на стартовую страницу")

def test_short_password_registration_fails(driver: ChromiumDriver):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    email = 'seva' + str(time.time()) + '@yandex.ru'
    # Поле Имя на странице регистрации
    driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys('Seva')
    # Поле Email на странице регистрации
    driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys(email)
    # Поле Пароль на странице регистрации
    driver.find_element(By.XPATH, ".//fieldset[3]/div/div/input").send_keys('12345')
    driver.find_element(By.XPATH, ".//form/button[text()='Зарегистрироваться']").click()
    # Надпись 'Некорректный пароль' на странице регистрации
    text = driver.find_element(By.XPATH, ".//div/main/div/form/fieldset[3]/div/p").text

    assert 'Некорректный пароль' in text
