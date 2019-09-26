from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/selects1.html')


num_1 = browser.find_element_by_xpath('//span[@id="num1"]')
x = num_1.text

num_2 = browser.find_element_by_xpath('//span[@id="num2"]')
y = num_2.text

z = str(int(x)+int(y))

select= Select(browser.find_element_by_tag_name("select"))
select.select_by_value(z)

button = browser.find_element_by_css_selector("button.btn")
button.click()
