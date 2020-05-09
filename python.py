from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
time.sleep(3)
driver.close()
