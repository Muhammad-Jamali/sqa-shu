from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://www.wikipedia.org/')
driver.implicitly_wait(10)
driver.maximize_window()

wait = WebDriverWait(driver, 10)

section = driver.find_element(By.XPATH, '//*[@id="www-wikipedia-org"]/div[7]/div[3]')

links = section.find_elements(By.TAG_NAME,'a')

for link in links:
    print(link.get_attribute('href'))
    link.click()
    sleep(5)
    print(driver.title)
    driver.back()
    sleep(5)




