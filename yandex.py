from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("https://yandex.ru/")         
browser.window_handles[0]

links = browser.find_elements_by_xpath("//a[not(contains(@href, 'yastatic'))]")

browser.execute_script("window.open('');")
browser.window_handles[1]

for href in links:
    link = href.get_attribute('href')
          
    browser.switch_to.window(browser.window_handles[1])
    browser.get(link)
    
    time.sleep(2) #введена, чтобы можно было визуально определить, что открылось. Делает скрипт дольше, при необходимости ускорения процесса можно закомментировать строку.
    
    browser.switch_to.window(browser.window_handles[0])
    


