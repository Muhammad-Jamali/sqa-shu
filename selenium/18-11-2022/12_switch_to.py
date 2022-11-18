from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(10)
driver.get('https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_submit_get')
driver.maximize_window()


#It will fail due to iFrame
#driver.find_element(By.XPATH, '/html/body/button').click()

driver.switch_to.frame('iframeResult')
driver.find_element(By.XPATH, '/html/body/button').click()

#focus back to default frame
driver.switch_to.default_content()

sleep(5)
