# 1program
# from selenium.webdriver import Chrome
# from time import sleep
# driver = Chrome('./chromedriver')
# driver.get('http://demowebshop.tricentis.com')
# driver.minimize_window()
# sleep(3)
# driver.maximize_window()
# sleep(3)
# curent_title = driver.title
# print(curent_title)
# url = driver.current_url
# print(url)
# driver.close()

# 2.program
# from selenium.webdriver import Chrome
# from time import sleep
# driver = Chrome('./chromedriver')
# driver.get('http://demowebshop.tricentis.com')
# driver.find_element_by_link_text('Register').click()
# sleep(2)
# driver.find_element_by_id('gender-male').click()
# sleep(3)
# driver.find_element_by_id('FirstName').send_keys('hello')
# sleep(3)
# driver.find_element_by_id('LastName').send_keys('word')
# sleep(3)
# driver.find_element_by_id('Email').send_keys('first.last@company.com')
# sleep(2)
# driver.find_element_by_id('Password').send_keys('Password134')
# sleep(2)
# driver.find_element_by_id('ConfirmPassword').send_keys('password123')
# sleep(3)
# driver.find_element_by_id('button-1 register-next-step-button').click()
# driver.close()

#3 program

# from selenium.webdriver import Chrome
# from time import sleep
# driver = Chrome('./chromedriver')
# driver.get('http://demowebshop.tricentis.com')
# driver.find_element_by_link_text('Log in').click()
# sleep(3)
# driver.find_element_by_id('Email').send_keys('sri.ram@gmail.com')
# sleep(3)
# driver.find_element_by_id('Password').send_keys('password12345')
# sleep(3)
# driver.find_elements_by_xpath("button-1 login-button").click()
# driver.close()
#
#4 program
# driver = Chrome('./chromedriver')
# driver.get("https://www.makemytrip.com/flights/?cmp=SEM|D|DF|G|Brand|B_M_Makemytrip_Variants|Brand-Variants-Exact|ETA|Regular|V2|529647798181&s_kwcid=AL!1631!3!529647798181!e!!g!!make%20my%20trip%2F&ef_id=EAIaIQobChMIsem15Iup9gIVh2kqCh1apQIsEAAYASAAEgLidfD_BwE:G:s&gclid=EAIaIQobChMIsem15Iup9gIVh2kqCh1apQIsEAAYASAAEgLidfD_BwE")
# sleep(3)
# driver.find_element_by_css_selector("li[data-cy='roundTrip']").click()
# sleep(3)
# driver.find_element_by_link_text('From').send_keys('delhi')
# sleep(3)
# driver.find_element_by_link_text('To').send_keys('banglore')
# sleep(3)
# driver.find_element_by_css_selector("span[class = 'lbl_input latoBold appendBottom10']").send_keys('4 march 22')
# sleep(3)
#driver.close(

#5 program
# from selenium.webdriver import Chrome
# from time import sleep
# driver = Chrome('./chromedriver')
# driver.get('file:///C:/Users/admin/Downloads/demo.html')
# sleep(3)
# element = driver.find_elements_by_name('fname')
# for item in element:
#     item.send_keys('firstname')
#     sleep(1)
# driver.close()

#6 program
# driver = Chrome('./chromedriver')
# driver.get('file:///C:/Users/admin/Downloads/demo.html')
# sleep(3)
# boxes = driver.find_element_by_name("download").click()
# sleep(2)

#7 program
# driver = Chrome('./chromedriver')
# driver.get('file:///C:/Users/admin/Downloads/demo.html')
# ele = driver.find_elements_by_name('download')
# sleep(2)
# for item in ele:
#     item.click()
#     sleep(1)

# driver = Chrome('./chromedriver')
# driver.get('file:///C:/Users/admin/Downloads/demo.html')
# sleep(2)
# ele = driver.find_elements_by_name('fname')
# for item in ele:
#     item.send_keys('firstname')
#     sleep(1)
# driver.close()


#
# driver = Chrome('./chromedriver')
# driver.get('file:///C:/Users/admin/Downloads/demo.html')
# driver.maximize_window()
# driver.find_element_by_id('firstname').send_keys('fnmae')
# driver.find_element_by_id('lastname').send_keys('lnamer')
# driver.find_element_by_id('submit').click()
# sleep(2)
# driver.close()

# driver = Chrome('./chromedriver')
# driver.get('file:///C:/Users/admin/Downloads/demo.html')
# ele = driver.find_elements_by_css_selector("input[name='fname']")
# sleep(2)
# for item in ele:
#     item.send_keys('sriram')
#     sleep(1)

# driver = Chrome('./chromedriver')
# driver.get('file:///C:/Users/admin/Downloads/loading.html')
# sleep(2)
# driver.find_element_by_css_selector("input[name='fname']").send_keys('sri')
# sleep(2)
# driver.find_elements_by_css_selector("input[name='lname']").send_keys('ram')
# sleep(2)
# driver.find_element_by_css_selector("input[value='Login']").click()
# sleep(1)

#
# driver = Chrome('./chromedriver')
# driver.get('http://demowebshop.tricentis.com/books')
# sleep(2)
# cart = driver.find_elements_by_xpath("//input[@value='Add to cart']")
# for item in cart:
#     item.click()
#     sleep(1)

#
# driver = Chrome('./chromedriver')
# driver.get('https://www.python.org/')
# sleep(2)
# elements = driver.find_elements_by_xpath("//a")
# for i in elements:
#     link_text = i.text.strip()
#     if 'python' in link_text:
#         print(link_text)

#
# driver = Chrome('./chromedriver')
# driver.maximize_window()
# driver.get('https://www.python.org/')
# sleep(2)
# ele = driver.find_elements_by_xpath("//a")
# for item in ele:
#     link_text = item.text.strip()
#     if 'python' in link_text:
#         print(link_text)

#
# driver = Chrome('./chromedriver')
# driver.maximize_window()
# driver.get('file:///C:/Users/admin/Downloads/demo.html')
# sleep(2)
#name = ['ALEX','AMY','BILL']
# res = driver.find_element_by_xpath(f"//td[text()='ALEX']/..//td[4]")
# print(res.text)
# for item in res:
#     print(item)

###########
# driver = Chrome('./chromedriver')
# driver.get('http://demowebshop.tricentis.com/')
# driver.get('file:///C:/Users/admin/Downloads/demo.html')
# driver.get('https://www.python.org/')
# driver.get('file:///C:/Users/admin/Downloads/demo.html')
# from selenium.webdriver.support.select import Select
# driver.maximize_window()
# sleep(2)

#######9
# cars = driver.find_element_by_id('standard_cars')
# s = Select(cars)
# s.select_by_visible_text('Audi')
# sleep(2)
# s.select_by_visible_text('Mercedes')
# sleep(2)
# s.select_by_index(5)
# sleep(2)
# s.select_by_value('for')
# all_option = s.options
# for item in
# all_option:
#     s.select_by_visible_text(item.text)
#     sleep(1)
####8
# james = "//div[@class='block block-popular-tags']//a"
# link = driver.find_elements_by_xpath(james)
# for i in link:
#     print(i.text)

#########7
# names = "//div[@class='footer-menu-wrapper']//a"
# link = driver.find_elements_by_xpath(names)
# for item in link:
#     print(item.text)

# link = driver.find_elements_by_xpath(names)
# for item in link:
#     print(item.text)
    #sleep(2)

#######6
# from selenium.webdriver import Chrome
# from time import sleep
# driver = Chrome('./chromedriver')
# xpath = ("//div[@class='block block-category-navigation']//a")
# links = driver.find_elements_by_xpath(xpath)
# for link in links:
#     print(link.text)
#     sleep(2)

#####5   [to click on good and radio button]
# driver.find_element_by_xpath("//label[text()='Good']/..//input[@type='radio']").click()
# sleep(2)

#######4    [to click on book and add to cart,to add books to shopping cart]
# driver.find_element_by_link_text('Books').click()
# sleep(2)
# list = ['Computing and Internet', 'Fiction', 'Health Book']
# for item in list:
#     ele = f"//a[text()='{item}']/../..//input[@value='Add to cart']"
#     print(ele)
#     driver.find_element_by_xpath(ele).click()
#     sleep(2)

########3    [to go python url and i want python 3.10.1 release notes]
# driver.find_element_by_link_text('Downloads').click()
# sleep(2)
# driver.find_element_by_xpath("//a[text()='Python 3.10.1']/../..//a[text()='Release Notes']").click()

#########2  [to click on particular click button]
# language = ['Ruby', 'Java', 'Perl', 'Python', 'C#', 'JavaScript']
# for i in language:
#     driver.find_element_by_xpath(f"//td[text()='{i}']/..//input[@name='download']").click()
#     sleep(2)

#########1   [to enter register and register login]
# driver.find_element_by_link_text('Register').click()
# sleep(2)
# driver.find_element_by_id('gender-male').click()
# sleep(1)
# driver.find_element_by_id('FirstName').send_keys('sri')
# sleep(1)
# driver.find_element_by_xpath("(//input[@class='text-box single-line'])[2]").send_keys('ram')
# sleep(1)
# driver.find_element_by_id("Email").send_keys('sri.ram@company.com')
# driver.find_element_by_id('register-button').click()

########window handling
# driver = Chrome('./chromedriver')
# driver.get("https://www.monsterindia.com/")
# sleep(2)
# driver.find_element_by_id("SE_home_autocomplete").send_keys('python')
# sleep(2)
# driver.find_element_by_xpath("//input[@value='Search']").click()
# sleep(2)
# driver.find_element_by_xpath("(//a[text()='Python -'])[1]").click()
# sleep(2)
# driver.quit()
#
######window handling
# from selenium.webdriver import Chrome
# from time import sleep
# driver = Chrome('./chromedriver')
# driver.get('http://demowebshop.tricentis.com')
# driver.maximize_window()
# sleep(2)
# driver.find_element_by_link_text("Simple Computer").click()
# sleep(2)
# driver.find_element_by_xpath("//title[text()='Twitter']").click()
# handles = driver.window_handles
# driver.switch_to.window(handles[1])
# driver.find_element_by_name("session[username_or_email]").send_keys('sriram')
# sleep(2)
# driver.find_element_by_xpath("//span[text()='Log in']").click()
# driver.close()
# driver = Chrome('./chromedriver')
# driver.get("https://www.amazon.com/")
# sleep(2)
# driver.find_element_by_xpath("//a[@class='nav-a']  ").click()
# sleep(2)

from selenium.webdriver import Chrome
from time import sleep
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
# driver = Chrome('./chromedriver')
# driver.get("file:///C:/Users/admin/Downloads/progressbar.html")
# sleep(2)
# driver.find_element_by_xpath("//button[text()='Click Me']").click()
# wait = WebDriverWait(driver, timeout=30)
# wait.until(expected_conditions.visibility_of_element_located(('xpath', "//div[text()='100%']")))
# print('done')

# from selenium.webdriver import Chrome
# from time import sleep
# driver = Chrome('./chromedriver')
# driver.get('http://demowebshop.tricentis.com')
# sleep(1)
# driver.find_element_by_xpath("//input[@value='Search']").click()
# sleep(2)
# print(driver.switch_to.alert.text)
# driver.switch_to.alert.accept()

# from selenium.webdriver import Chrome
# from time import sleep
# driver = Chrome('./chromedriver')
# driver.get("https://www.goibibo.com/")
# sleep(2)
# driver.find_element_by_xpath("//span[text()='Departure']").click()
# sleep(2)
# driver.find_element_by_xpath("//div[text()='April 2022']/../..//p[text()='20']").click()
# sleep(1)
# driver.find_element_by_xpath("//span[@class='fswTrvl__done']").click()
# sleep(1)
# driver.find_element_by_xpath("//span[text()='SEARCH FLIGHTS']").click()

#wap to click on (x)button
# from selenium.webdriver import Chrome
# from time import sleep
# driver = Chrome('./chromedriver')
# driver.get("https://www.monsterindia.com/")
# sleep(2)
# driver.find_element_by_xpath("//span[text()='Upload Resume']").click()
# sleep(2)
# driver.find_element_by_xpath("(//div[@class='close-button mqfi-cross'])[2]").click()
# sleep(3)
# driver.find_element_by_xpath("(//input[@id='file-upload'])[2]").send_keys(r"C:\Users\admin\PycharmProjects\Alpha_3\files_directory\txt_log_files\sample.txt")
# sleep(2)

# a = driver.find_element_by_xpath("//a[text()='Apple']").is_enabled()

# from selenium.webdriver import Chrome
# from time import sleep
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.action_chains import ActionChains
# driver = Chrome('./chromedriver')
# driver.get('file:///C:/Users/admin/Downloads/demo.html')
# sleep(2)
# cars = driver.find_element_by_id('standard_cars')
# s = Select(cars)
# all_options = s.options
# s.select_by_visible_text('Audi')
# sleep(3)
# s.select_by_visible_text('Honda')
# sleep(3)
# s.select_by_index(3)
# sleep(2)
# s.select_by_value('nin')
# for i in all_options:
#     s.select_by_visible_text(i.text)
#     sleep(1)

# from selenium.webdriver import Chrome
# from time import sleep
# from selenium.webdriver.support.expected_conditions import visibility_of_element_located
# from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.support.ui import WebDriverWait
# def outer(func):
#     def wrapper(*args, **kwargs):
#         locator = args[0]
#         w = WebDriverWait(driver, 20)
#         v = visibility_of_element_located(locator)
#         w.until(v)
#         func(*args, **kwargs)
#     return wrapper
#
# class _visibility_of_element_located(visibility_of_element_located):
#     def __call__(self, driver):
#         res = super().__call__(driver)
#         if isinstance(res, WebElement):
#             return res.is_enabled()
#         else:
#             False
#
# @outer
# def click_element(locator):
#     driver.find_element(*locator).click()
# @outer
# def enter_text(locator, value):
#     driver.find_element(*locator).clear()
#     driver.find_element(*locator).send_keys(value)
#
# driver = Chrome('./chromedriver')
# driver.get('http://demowebshop.tricentis.com')
# sleep(2)
# # driver.maximize_window()
# sleep(5)
# click_element(("xpath", "//a[@class='ico-register']"))
# click_element(("id", "gender-male"))
# enter_text(("id", "FirstName"), 'sri')
# enter_text(("id", "LastName"), 'ram')
# enter_text(("id", "Email"), 'sri.ram@company.com')
# enter_text(("id", "Password"), 'password123')
# enter_text(("id", "ConfirmPassword"), 'password123')
# click_element(("id", "register-button"))


# from selenium.webdriver import Chrome
# from time import sleep
# from selenium.webdriver.support.select import Select
# driver = Chrome('./chromedriver')
# driver.get('http://demowebshop.tricentis.com')
# sleep(2)
# driver.get("file:///C:/Users/admin/Downloads/demo.html")
# cars = driver.find_element_by_id('standard_cars')
# s = Select(cars)
# s.select_by_visible_text('BMW')
# s.select_by_index(3)
# s.select_by_value('aud')
# res = driver.find_elements_by_xpath("//div[@class='title']/..//a")
# for i in res:
#     print(i.text)
# res = driver.find_elements_by_xpath("//div[@class='title']/..//a")
# for i in res:
#     print(i.text)
# res =driver.find_element_by_xpath("//input[@name='fname']")
# for i in res:
#     i.send_keys('sriram')

# from selenium.webdriver import Chrome
# from time import sleep
# driver = Chrome('./chromedriver')
# driver.get('http://demowebshop.tricentis.com')
# sleep(2)
# driver.find_element_by_xpath("(//a[contains(text(), 'Books')])[3]").click()
# sleep(2)
# driver.find_element_by_xpath("//a[text()='Computing and Internet']/../..//input[@value='Add to cart']").click()

# from selenium.webdriver import Chrome
# from time import sleep
# driver = Chrome('./chromedriver')
# driver.get("http://demowebshop.tricentis.com/")
# sleep(2)
# driver.find_element_by_xpath("//a[text()='Health Book'/../..//input[@value='Add to Cart']")
# sleep(3)

# from selenium.webdriver import Chrome
# from time import sleep
# driver = Chrome('./chromedriver')
# driver.get('http://demowebshop.tricentis.com/')
# sleep(2)
# driver.find_element_by_link_text('Log in').click()
# sleep(2)
# driver.find_element_by_id('Email').send_keys('sri.ram@gmail.com')
# sleep(2)
# driver.find_element_by_id('Password').send_keys('password123')
# sleep(2)
# driver.find_element_by_css_selector("input[value='Log in']").click()

# driver.find_element_by_xpath("//a[text()='14.1-inch Laptop']/../..//input[@value='Add to cart']").click()

# driver.find_element_by_tag_name('img').click()

# driver.find_element_by_link_text('Books').click()
# driver.find_element_by_xpath("//a[text()='Fiction']/../..//input[@value='Add to cart']").click()

# driver.find_element_by_xpath("//input[@type='radio']/..//label[text()='Good']").click()



# from selenium.webdriver import Chrome
# from time import sleep
# driver = Chrome('./chromedriver')
# driver.get('http://demowebshop.tricentis.com/')
# sleep(2)
# driver.maximize_window()
# sleep(3)
# driver.find_element_by_link_text('Register').click()
# sleep(1)
# driver.find_element_by_id('gender-male').click()
# driver.find_element_by_id('FirstName').send_keys('sri')
# driver.find_element_by_id('LastName').send_keys('ram')
# driver.find_element_by_id('Email').send_keys('sriram@gmail.com')
# driver.find_element_by_id('Password').send_keys('passward123')
# driver.find_element_by_id('ConfirmPassword').send_keys('passward123')
# driver.find_element_by_id('register-button').click()

# from selenium.webdriver import Chrome
# from time import sleep
# driver = Chrome('./chromedriver')
# driver.get('http://demowebshop.tricentis.com/register')
# driver.find_element_by_css_selector("a[class='ico-login']").click()
# driver.find_element_by_xpath("//input[@class='email']").send_keys('sriram@gmail.com')
# driver.find_element_by_id('Password').send_keys('password123')
# driver.find_element_by_xpath("//input[@value='Log in']").click()

# from selenium.webdriver import  Chrome
# driver = Chrome('./chromedriver')
# driver.get('http://demowebshop.tricentis.com/')
# driver.find_element_by_xpath("//a[text()='14.1-inch Laptop']/../..//input[@value='Add to cart']").click()

# from selenium.webdriver import Chrome
# driver = Chrome('./chromedriver')
# driver.get('http://demowebshop.tricentis.com/')
# driver.find_element_by_xpath("//label[text()='Good']/..//input[@type='radio']").click()

# from selenium.webdriver import Chrome
# driver = Chrome('./chromedriver')
# driver.get('file:///C:/Users/admin/Downloads/demo.html')
# items = driver.find_elements_by_xpath("//input[@type='checkbox']")
# for i in items:
#     i.click()

# from selenium.webdriver import Chrome
# driver = Chrome('./chromedriver')
# driver.get('https://www.python.org/')
# driver.find_element_by_link_text('Downloads').click()
# ex = driver.find_element_by_xpath("//a[text()='Python 3.8.13']/../..//a[text()='Release Notes']").click()
# for i in ex:
#     print(i.text)

# from selenium.webdriver import Chrome
# from time import sleep
# driver = Chrome('./chromedriver')
# driver.get('http://demowebshop.tricentis.com/')
# driver.find_element_by_xpath("(//a[contains(text(), 'Books')])[3]").click()
# books = ['Computing and Internet', 'Fiction', 'Health Book']
# for item in books:
#     xpath = f"//a[text()='{item}']/../..//input[@value='Add to cart']"
#     driver.find_element_by_xpath("//a[text()='{item}']/../..//input[@value='Add to cart']").click()
#     sleep(2)\

# from selenium.webdriver import Chrome
# driver =  Chrome('./chromedriver')
# driver.get('http://demowebshop.tricentis.com/')
# list = ['Excellent', 'Good', 'Poor', 'Very bad']
# for item in list:
#     xpath = f"//label[text()='{item}']/..//input[@type='radio']"
#     driver.find_element_by_xpath(xpath).click()
#     sleep(2)

# from selenium.webdriver import Chrome
# driver = Chrome('./chromedriver')
# driver.get("https://www.ajio.com/shop/sale?gclid=EAIaIQobChMIlPCkyPfT9gIVI5JmAh078wVeEAAYASAAEgJcR_D_BwE")
# driver.find_element_by_xpath("//input[@placeholder='Search AJIO']").send_keys("glass for men")
# driver.find_element_by_xpath("//span[@class='ic-search']").click()
# sleep(2)
# names = driver.find_elements_by_xpath("//div[@class='nameCls']")
# value = driver.find_elements_by_xpath("//span[@class='price  ']")
# p = [item.text for item in names]
# o = [item.text for item in value]
# print(p)
# print(o)
# p = []
# import re
# for i in o:
#     res = re.findall(r'\d', i)
#     p.append(''.join(res))
# print(p)
#
# run = max(p)
# print(run)

# from selenium.webdriver import Chrome
# driver =  Chrome('./chromedriver')
# driver.get('http://demowebshop.tricentis.com/')
# path = "//div[@class='block block-category-navigation']"
# run = driver.find_elements_by_xpath(path)
# for i in run:
#     print(i.text)
#
# p = "//div[@class='footer-menu-wrapper']"
# o = driver.find_elements_by_xpath(p)
# for i in o:
#     print(i.text)

# from selenium.webdriver import Chrome
# driver = Chrome('./chromedriver')
# driver.get('https://www.monsterindia.com/')
# driver.find_element_by_xpath("//input[@placeholder='Search by Skills, Company & Job Title']").send_keys('python jobs')
# driver.find_element_by_xpath("//input[@value='Search']").click()
# r = driver.find_elements_by_xpath("//a[text()='Python Developer Required']")
# for i in r:
#     print(i.text)

# from selenium.webdriver import Chrome
# driver = Chrome('./chromedriver')
# driver.get('https://www.myntra.com/')
# driver.find_element_by_xpath("//input[@placeholder='Search for products, brands and more']").send_keys('tshirts')
# driver.find_element_by_xpath("//span[@class='myntraweb-sprite desktop-iconSearch sprites-search']").click()
# item = driver.find_elements_by_xpath("//h4[@class='product-product']")
# price = driver.find_elements_by_xpath("//span[@class='product-discountPercentage']")
# p = [i.text for i in item]
# o = [i.text for i in price]
# print(p)
# print(o)

# from selenium.webdriver import Chrome
# driver = Chrome('./chromedriver')
# driver.get('https://www.myntra.com/')
# driver.find_element_by_xpath("//input[@placeholder='Search for products, brands and more']").send_keys('tshirts')
# driver.find_element_by_xpath("//span[@class='myntraweb-sprite desktop-iconSearch sprites-search']").click()
# items = driver.find_elements_by_xpath("//span[@class='product-discountedPrice']")
#
# r = [i.text for i in items]
# print(r)

# from selenium.webdriver import Chrome
# driver = Chrome('./chromedriver')
# driver.get('file:///C:/Users/admin/Downloads/demo.html')
# p = driver.find_elements_by_xpath("//input[@name='fname']")
# for item in p:
#     item.send_keys('sriram')

# from selenium.webdriver import Chrome
# from selenium.webdriver.support.select import Select
# driver = Chrome('./chromedriver')
# driver.get('file:///C:/Users/admin/Downloads/demo.html')
# p = driver.find_element_by_id("standard_cars")
# s = Select(p)
# sel = s.options
# s.select_by_visible_text('Audi')
# s.select_by_index(3)
# s.select_by_value('jgr')
# for i in sel:
#     print(i.text)

# from selenium.webdriver import Chrome
# from selenium.webdriver.support.select import Select
# driver = Chrome('./chromedriver')
# driver.get('file:///C:/Users/admin/Downloads/demo.html')
# cars = driver.find_element_by_id('standard_cars')
# s =Select(cars)
# # all= s.options
# # for i in all:
# #     s.select_by_visible_text(i.text)
# s.deselect_by_visible_text('Ford')

# from selenium.webdriver import Chrome
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.expected_conditions import visibility_of_element_located
# driver = Chrome('./chromedriver')
# driver.get('file:///C:/Users/admin/Downloads/demo.html')
# driver.find_element_by_id("firstname").send_keys('sriram')
# # wait = WebDriverWait(driver, 10)
# v = visibility_of_element_located(driver)
# wait.until(v)

# from selenium.webdriver import Chrome
# from selenium.webdriver.common.action_chains import ActionChains
# driver = Chrome('./chromedriver')
# driver.get('https://www.monsterindia.com/')
# action = ActionChains(driver)
# run = driver.find_element_by_xpath("(//a[@data-check='menutab'])[1]")
# action.move_to_element(run).perform()
# jobs_by_title = driver.find_element_by_xpath("//a[text()='Jobs by Title']")
# action.move_to_element(jobs_by_title).perform()


# pre = driver.find_element_by_xpath("""//a[@onclick='window.homeBehavior.home.common.trackHeaderTopLinkChildResponse(event, "Jobs by Title","Android Developer Jobs")']""")
# action.move_to_element(pre).perform()
# pre.click()

# from selenium.webdriver import Chrome
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# driver = Chrome('./chromedriver')
# driver.get('https://www.monsterindia.com/')
# actions = ActionChains(driver)
# actions.send_keys(Keys.PAGE_DOWN)
#
# driver.find_element_by_xpath("//span[@title='Python']").click()

# from selenium.webdriver import Chrome
# from selenium.webdriver.common.action_chains import ActionChains
# driver = Chrome('./chromedriver')
# driver.get('https://www.monsterindia.com/')
# action = ActionChains(driver)
# item = driver.find_element_by_xpath("(//a[@data-check='menutab'])[1]")
# action.move_to_element(item).perform()
# p = driver.find_element_by_xpath("//a[text()='Jobs by Location']")
# action.move_to_element(p).perform()
# o = driver.find_element_by_xpath("""//a[@onclick='window.homeBehavior.home.common.trackHeaderTopLinkChildResponse(event, "Jobs by Location","Jobs in Bangalore")']""")
# action.move_to_element(o).perform()
# o.click()

# from selenium.webdriver import Chrome
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.expected_conditions import visibility_of_element_located
# from selenium.webdriver.support import expected_conditions
# driver = Chrome('./chromedriver')
# driver.get('file:///C:/Users/admin/Downloads/demo.html')
# wait = WebDriverWait(driver, 10)
# wait.until(expected_conditions.visibility_of_element_located(driver.find_element_by_id('firstname').send_keys('sriram')))
# # v = visibility_of_element_located('id', 'Firstname ')
# # wait.until(v)
# driver.find_element_by_id('firstname').send_keys('sriram')

# from selenium.webdriver import Chrome
# from selenium.webdriver.common.action_chains import ActionChains
# driver = Chrome('./chromedriver')
# driver.get('https://www.monsterindia.com/')
# action = ActionChains(driver)
# item = driver.find_element_by_xpath("(//a[@data-check='menutab'])[1]")
# action.move_to_element(item).perform()
# p = driver.find_element_by_xpath("//a[text()='Jobs by Location']")
# action.move_to_element(p).perform()
# o = driver.find_element_by_xpath("(//a[contains(text(), 'Jobs in Chennai')])[1]")
# action.move_to_element(o).perfrom()

