from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time 

service_obj = Service("C:/Python310/Scripts/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://uibank.uipath.com/register-account")
driver.maximize_window()

txt_firstname = driver.find_element(By.ID,"firstName")
txt_firstname.send_keys("Gulraiz")

ddl_title = Select(driver.find_element(By.ID,"title"))
ddl_title.select_by_visible_text("Mr")
#ddl_title.select_by_index(0)
#ddl_title.select_by_value('mr')

txt_middlename = driver.find_element(By.XPATH, "//*[@id='middleName']")
txt_middlename.send_keys("Engr.")

heading = driver.find_element(By.CLASS_NAME, "text-center").text
print(heading)

time.sleep(5)

login_link = driver.find_element(By.LINK_TEXT, "Login")
login_link.click()

time.sleep(5)