from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Remove implicit wait and check the results
# It works only for the presense of element 
# But does not wait for elemenet to be interactible
driver.implicitly_wait(10)
driver.get('https://www.google.com')

txt_search = driver.find_element(By.CSS_SELECTOR, 'input[name="q"]')
txt_search.send_keys('weather today')


btn_search = driver.find_element(By.CSS_SELECTOR, 'input[name="btnK"]')
btn_search.click()



# e_wait = WebDriverWait(driver,5)
# condition = EC.presence_of_element_located((By.XPATH, '//*[@id="wob_tm"]'))
# txt_weather = e_wait.until(condition)


#Explicit Wait
txt_weather = WebDriverWait(driver,5).until(EC.presence_of_element_located(
    (By.XPATH, '//*[@id="wob_tm"]')
))


print(txt_weather.text)




