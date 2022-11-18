from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(10)
driver.get('https://demo.automationtesting.in/Alerts.html')
driver.maximize_window()

btn = driver.find_element(By.XPATH, '//*[@id="OKTab"]/button')
btn.click()

sleep(5)

alert = Alert(driver)
alert.accept()

#driver.switch_to.alert.accept()
#driver.switch_to.default_content()


#print(alert.text)

sleep(5)
