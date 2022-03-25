# from selenium.webdriver import Chrome
# from time import sleep
# from selenium.webdriver.support.select import Select
# driver = Chrome('./chromedriver')
# driver.get('file:///C:/Users/admin/Downloads/demo.html')
# sleep(2)
# c = driver.find_element_by_id('standard_cars')
# s = Select(c)
# all_options = s.options
# for i in all_options:
    #for clicking whole list box
    # i.click()
    # sleep(1)
    #for printing whole list box values
    # print(i.text)
# s.select_by_visible_text('BMW')
# sleep(2)
# s.select_by_visible_text('Mercedes')
# sleep(2)
# s.select_by_index(6)
# s.select_by_index(1)
# sleep(1)
# s.select_by_value('min')
# sleep(1)
# s.select_by_value('lr')

#selecting the item and printing the selected item
from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.select import Select
driver = Chrome('./chromedriver')
driver.get('file:///C:/Users/admin/Downloads/demo.html')
sleep(2)
c = driver.find_element_by_id('standard_cars')
s = Select(c)
s.select_by_visible_text('Audi')
current = s.first_selected_option.text
print(current)
s.select_by_visible_text('Jaguar')
current = s.first_selected_option.text
print(current)
sleep(2)



