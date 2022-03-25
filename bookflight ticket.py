# from selenium.webdriver import Chrome
# from time import sleep
# driver = Chrome('./chromedriver')
# driver.get('https://www.makemytrip.com/')
# sleep(2)
# driver.find_element_by_xpath("//span[text()='DEPARTURE']").click()
# sleep(2)
# driver.find_element_by_xpath("//div[text()='April 2022']/../..//p[text()='20']").click()


# from selenium.webdriver import Chrome
# from time import sleep
# driver = Chrome('./chromedriver')
# driver.get("https://www.goibibo.com/")
# sleep(2)
# driver.find_element_by_link_text("Enter city or airport").send_keys('kempagowda airport')
# sleep(1)
# driver.find_element_by_link_text("Enter city or airport").send_keys('hubbali airport')
# sleep(1)
# driver.find_element_by_xpath("//span[text()='Departure']").click()
# sleep(2)
# driver.find_element_by_xpath("//div[text()='April 2022']/../..//p[text()='20']").click()
# sleep(1)
# driver.find_element_by_xpath("//span[@class='fswTrvl__done']").click()
# sleep(1)
# driver.find_element_by_xpath("//span[text()='SEARCH FLIGHTS']").click()



from selenium.webdriver import Chrome
from time import sleep

driver = Chrome('./chromedriver')
driver.get('https://www.ajio.com/')
sleep(2)
driver.find_element_by_xpath("//input[@name='searchVal']").send_keys('shoes')
sleep(1)
driver.find_element_by_xpath("//span[@class='ic-search']").click()
sleep(1)
# shoes = driver.find_elements_by_xpath("//div[@class='contentHolder']")
ele_shoes = driver.find_elements_by_xpath("//div[@class='nameCls']")
ele_price = driver.find_elements_by_xpath("//span[@class='price  ']")

shoename = [item.text for item in ele_shoes]
shoeprice = [item.text for item in ele_price]

pairs = []
import re
for pair in ele_price:
    res = re.findall(r'\d', pair)
    pairs.append(int(''.join(res)))
print(pairs)

# for shoe, price in zip(shoename, shoeprice):
#     pairs.append(shoename, shoeprice)