from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support import expected_conditions
# driver = Chrome('./chromedriver')
# driver.get('file:///C:/Users/admin/Downloads/loading.html')
# wait = WebDriverWait(driver, 20)
# wait.until(expected_conditions.visibility_of_element_located(('name', 'fname')))
# driver.find_element_by_name('fname').send_keys('sriram')


#wait for progress bar to complete 100%
from time import sleep
# driver = Chrome('./chromedriver')
# driver.get('file:///C:/Users/admin/Downloads/progressbar.html')
# sleep(2)
# driver.find_element_by_xpath("//button[text()='Click Me']").click()
#
# wait = WebDriverWait(driver, 30)
# wait.until(expected_conditions.visibility_of_element_located(('xpath', "//div[text()='100%']")))
# print('done')


