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
driver.get('https://dribbble.com/')
driver.maximize_window()


# btn_close = WebDriverWait(driver,5).until(EC.presence_of_element_located(
#     (By.XPATH, '//*[@id="elementor-popup-modal-26600"]/div/div[4]')
# ))

# sleep(2)

# btn_close.click()

# sleep(2)

menu = driver.find_element(By.XPATH, "//a[@data-site-nav-element='Inspiration']")

action = ActionChains(driver)

action.move_to_element(menu).perform()

sleep(2)


# driver.find_element(By.XPATH,'//*[@id="menu-item-27619"]/a').click()





