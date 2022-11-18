from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep
import os

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(10)
driver.get('https://uibank.uipath.com/')
driver.maximize_window()

sleep(3)

# driver.save_screenshot("./18-11-2022/screenshots/sample.png")

#Full Page Screenshot

# S = lambda X: driver.execute_script('return document.body.parentNode.scroll' +X)
# driver.set_window_size(S('Width'), S('Height'))
# driver.find_element(By.TAG_NAME, 'body').screenshot('./18-11-2022/screenshots/full_page.png')




