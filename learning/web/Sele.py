#!  python3
#   Sele.py Using selenium to control the browser
#   ADD explicit waits instead of time.sleep()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()
time.sleep(3)    #   LET the browser load

browser.get('https://selenium-python.readthedocs.io/')
time.sleep(1)

try:
    link = browser.find_element(By.LINK_TEXT, '4.2. Locating by Name')
    link.click()
except:
    raise ('There was no link to click')

#browser.send_keys('')

toClose = input();
browser.close()
browser.quit()
