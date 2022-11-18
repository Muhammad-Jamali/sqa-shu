from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep

chrome_options = webdriver.ChromeOptions()

prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.headless = True

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=chrome_options)

driver.implicitly_wait(10)
driver.get('https://uibank.uipath.com/')
driver.maximize_window()

sleep(3)

print(driver.title)







