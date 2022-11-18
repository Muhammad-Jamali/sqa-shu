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
driver.get('https://demo.automationtesting.in/Static.html')
driver.maximize_window()

draggable = driver.find_element(By.ID, 'angular')
droppable = driver.find_element(By.ID, 'droparea')


action = ActionChains(driver)
action.drag_and_drop(draggable,droppable).perform()

sleep(2)
