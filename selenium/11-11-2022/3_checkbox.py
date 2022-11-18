from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time 

service_obj = Service("C:/Python310/Scripts/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")


# #foreach

# arr = [1,2,3,4]
# checkboxes = [chk1,chk2,chk2]

# for i in arr:
#     print(item)

# for checkbox in checkboxes:
    # if checkbox.get_attribute('value') == "option1":
    #     checkbox.click()
    #     break


#thanwar
# for checkbox in checkboxes:
#     if checkbox.get_attribute('value') == "option1":
#         checkbox.click()
#     elif checkbox.get_attribute('value') == "option3":
#         checkbox.click()


# jamali
# options = ['option1', 'option2']

# for checkbox in checkboxes:
#     value = checkbox.get_attribute('value')
#     if  options.__contains__(value):
#         checkbox.click()
#     else:
#         break
        
        

time.sleep(5)