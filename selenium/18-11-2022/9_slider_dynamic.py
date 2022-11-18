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
driver.get('https://demo.automationtesting.in/Slider.html')
driver.maximize_window()

slider = driver.find_element(By.XPATH, '//*[@id="slider"]')

location = slider.location
size = slider.size

w,h = size['width'],size['height']

print(location)
print(size)

print(w,h)

action = ActionChains(driver)
action.drag_and_drop_by_offset(slider,w/4,0).perform()

sleep(2)





