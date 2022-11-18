from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:/Python310/Scripts/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://uibank.uipath.com/")

driver.maximize_window()

print(driver.title)
print(driver.current_url)

driver.get("https://uibank.uipath.com/register-account")

driver.minimize_window()
#driver.back()
#driver.refresh()
#driver.forward()

driver.close()