from selenium.webdriver import Chrome
from time import sleep
# driver = Chrome('./chromedriver')
# driver.get('http://demowebshop.tricentis.com/')
# sleep(3)
# driver.find_element_by_link_text("Books").click()
# sleep(2)
# driver.find_element_by_xpath("//a[text()='Computing and Internet']/../..//input[@value='Add to cart']").click()



"""do login in flipkart"""
# driver = Chrome('./chromedriver')
# driver.get('https://www.flipkart.com/')
# sleep(3)
# driver.find_element_by_link_text("Login").click()
# sleep(2)
# driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys('sri.ram@gmail.com')
# sleep(2)
# driver.find_element_by_xpath("//input[@type='password']").send_keys('password123')
# sleep(2)
# driver.find_element_by_xpath("(//button[@type='submit'])[2]").click()


"""do search tshits in amazon"""
# driver = Chrome('./chromedriver')
# driver.get("https://www.amazon.com/")
# sleep(2)
# driver.find_element_by_id("twotabsearchtextbox").send_keys('tshirts')
# driver.find_element_by_id("nav-search-submit-button").click()

"""click xpath of radio button correspounding to good"""
# driver = Chrome('./chromedriver')
# driver.get('http://demowebshop.tricentis.com/')
# sleep(2)
# driver.find_element_by_xpath("//label[text()='Good']/..//input[@type='radio']").click()

"""print all text in categaries"""
# driver = Chrome('./chromedriver')
# driver.get('http://demowebshop.tricentis.com/')
# res = driver.find_elements_by_xpath("//div[@class='title']/..//a")
# for i in res:
#     print(i.text)

