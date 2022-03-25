from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
def outer(func):
    def wrapper(*args, **kwargs):
        locator = args[0]
        w = WebDriverWait(driver, 20)
        v = visibility_of_element_located(locator)
        w.until(v)
        func(*args, **kwargs)
    return wrapper

class _visibility_of_element_located(visibility_of_element_located):
    def __call__(self, driver):
        res = super().__call__(driver)
        if isinstance(res, WebElement):
            return res.is_enabled()
        else:
            False

@outer
def click_element(locator):
    driver.find_element(*locator).click()
@outer
def enter_text(locator, value):
    driver.find_element(*locator).clear()
    driver.find_element(*locator).send_keys(value)


click_element(("xpath", "//a[@class='ico-register']"))
click_element(("id", "gender-male"))
enter_text(("id", "FirstName"), 'sri')
enter_text(("id", "LastName"), 'ram')
enter_text(("id", "Email"), 'sri.ram@company.com')
enter_text(("id", "Password"), 'password123')
enter_text(("id", "ConfirmPassword"), 'password123')
click_element(("id", "register-button"))