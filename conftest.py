import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='function')
def driver():
    path = "/Users/seva/Documents/PycharmProjects/WebDriver/bin/chromedriver"
    service = Service(path)
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://stellarburgers.nomoreparties.site")
    driver.maximize_window()
    yield driver
    driver.quit()

