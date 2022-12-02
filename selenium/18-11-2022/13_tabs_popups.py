from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(10)
driver.get('https://uibank.uipath.com/')
driver.maximize_window()

#body = driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + 't')

driver.execute_script("window.open('https://uibank.uipath.com/register-account')")


windows = driver.window_handles

for window in windows:
    print(window)

sleep(5)

driver.switch_to.window(driver.window_handles[0])

sleep(5)

driver.close()

sleep(3)





