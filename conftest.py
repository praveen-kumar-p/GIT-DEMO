from selenium.webdriver import Chrome
from time import sleep
from pytest import fixture

@fixture
def setup():
    driver = Chrome('./chromedriver')
    driver.get('http://demowebshop.tricentis.com')
    sleep(2)
    yield driver
    driver.close()