# from selenium.webdriver import Chrome
# from time import sleep
# import csv
# import re
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.expected_conditions import visibility_of_element_located
# from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.color import Color
# from selenium.webdriver.common.by import By
# class _visibiity_of_element_locator(visibility_of_element_located):
#     def __call__(self, driver):
#         result = super().__call__(driver)
#         if isinstance(result, WebElement):           #or
#         # if result == True:         #or       #element is loaded in DOM and visible on webpage
#             return result.is_enabled()
#         else:
#             return False
#
# def wait(func):
#     def wrapper(*args, **kwargs):
#         locator = args[0]
#         wait = WebDriverWait(driver, 20)
#         v = visibility_of_element_located(locator)
#         wait.until(v)
#         return func(*args, **kwargs)
#     return wrapper
#
# @wait
# def click_element(locator):
#     driver.find_element(*locator).click()
#
# @wait
# def enter_text(locator, value):
#     driver.find_element(*locator).clear()
#     driver.find_element(*locator).send_keys(value)
#
# @wait
# def select_item(*locator, item):
#     element = driver.find_element(*locator)
#     s = Select(element)
#     if isinstance(item, str):
#         s.select_by_visible_text(item)
#     elif isinstance(item, int):
#         s.select_by_index(item)
#     else:
#         raise TypeError
#
# driver = Chrome('./chromedriver')
# driver.get(('http://demowebshop.tricentis.com'))
# sleep(2)
# click_element(('link text', 'Register'))
# sleep(1)
# click_element(('id', 'gender-male'))
# sleep(1)
# enter_text(('name', 'FirstName'), 'hello')
# sleep(2)
# enter_text(('name', 'LastName'), 'world')
# sleep(2)
# enter_text(('id', 'Email'), 'hello.world@company.com')
# sleep(2)
# enter_text(('id', 'Password'), 'Password123')
# sleep(2)
# enter_text(('id', 'ConfirmPassword'), 'Password123')
# sleep(2)
# click_element(('id', 'register-button'))
# sleep(2)
# # driver.close()