from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import time


#Service obj = new Service()

service_obj = Service("C:/Python310/Scripts/chromedriver")

#provided value via constructor
chrome = webdriver.Chrome(service=service_obj)
chrome.service

#provided value via properties
#driver.service = service_obj

chrome.get("https://uibank.uipath.com/register-account")
chrome.maximize_window()

print(chrome.title)
print(chrome.current_url)

#chrome.back()
#chrome.forward()
#chrome.refresh()

txtFirstName = chrome.find_element(By.ID,"firstName")
txtFirstName.send_keys("Gulraiz")

ddlTitle = chrome.find_element(By.ID,"title")
#ddlTitle.send_keys("Mr")

Select(ddlTitle).select_by_visible_text("Mr")

time.sleep(3)

lnkLogin = chrome.find_element(By.LINK_TEXT,"Login")
lnkLogin.click()

time.sleep(5)





