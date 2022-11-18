from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time 


service_obj = Service("C:/Python310/Scripts/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

driver.implicitly_wait(5)

sum1 = driver.find_element(By.ID,'sum1')
sum2 = driver.find_element(By.ID,'sum2')

sum1.send_keys(Keys.NUMPAD1, Keys.NUMPAD2)
sum2.send_keys(12)

btnGetTotal = driver.find_element(By.XPATH, "//*[@id='gettotal']/button")
btnGetTotal.click()

time.sleep(5)



