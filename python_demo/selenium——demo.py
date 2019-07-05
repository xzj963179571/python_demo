from selenium import webdriver
from time import sleep
import unittest
driver = webdriver.Firefox() #Chrome
driver.get("http://www.baidu.com")
driver.find_element_by_id('kw').send_keys("selenium")
driver.find_element_by_id('su').click()
sleep(2)
title = driver.title
print(title)
driver.quit()

