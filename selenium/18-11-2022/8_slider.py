from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(10)
driver.get('https://demos.jquerymobile.com/1.4.2/rangeslider/')
driver.maximize_window()

slider = driver.find_element(By.XPATH, '//*[@id="ui-page-top"]/div[1]/div[3]/div[1]/form/div/div/div[2]/a[1]')

action = ActionChains(driver)
action.drag_and_drop_by_offset(slider,-100,0).perform()

sleep(2)





