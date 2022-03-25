from selenium.webdriver import Chrome
from time import sleep
driver = Chrome('./chromedriver')
driver.get('file:///C:/Users/admin/Downloads/demo.html')

"""to enter more than 1 name"""
# res = driver.find_elements_by_xpath("//input[@name='fname']")
# for i in res:
#     i.send_keys("sriram")

"""to enter 1 name"""
driver.find_element_by_xpath("//input[@name='fname']").send_keys("sriram")