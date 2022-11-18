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

dropdown = driver.find_element(By.ID,'searchLanguage')

select = Select(dropdown)
select.select_by_value('ko')

options = driver.find_elements(By.TAG_NAME, 'option')

for option in options:
    print(option.text + ":" + option.get_attribute('lang'))

print("Total: ", len(options))

sleep(5)


