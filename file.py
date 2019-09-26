from selenium import webdriver
import os

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/file_input.html')

browser.find_element_by_css_selector('[name="firstname"]').send_keys('Margarita')
browser.find_element_by_css_selector('[name="lastname"]').send_keys('Kornysheva')
browser.find_element_by_css_selector('[name="email"]').send_keys("snetkova28@gmail.com")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

browser.find_element_by_id('file').send_keys(file_path)

button = browser.find_element_by_tag_name("button")
button.click()
