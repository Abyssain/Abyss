from selenium import webdriver
import math

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/execute_script.html')

valuex = browser.find_element_by_css_selector('#input_value')
x = valuex.text

browser.find_element_by_css_selector('#answer').send_keys(str(math.log(abs(12*math.sin(int(x))))))

button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

browser.find_element_by_css_selector('#robotCheckbox').click()
browser.find_element_by_css_selector('#robotsRule').click()

button.click()
