from selenium import webdriver
import math

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/alert_accept.html')

browser.find_element_by_tag_name('button').click()
confirm = browser.switch_to.alert
confirm.accept()

valuex = browser.find_element_by_css_selector('#input_value')
x = valuex.text

browser.find_element_by_css_selector('#answer').send_keys(str(math.log(abs(12*math.sin(int(x))))))
browser.find_element_by_tag_name("button").click()
