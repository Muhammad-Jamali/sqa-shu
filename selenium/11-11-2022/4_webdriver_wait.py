from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service_obj = Service("C:/Python310/Scripts/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get('https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html')

#The wait will be applied to all elements
driver.implicitly_wait(8)

btnDownload = driver.find_element(By.ID,"downloadButton")
btnDownload.click()

#progress_element = driver.find_element(By.CLASS_NAME, "progress-label")

# WebDriverWait(driver,30).until(
#     EC.text_to_be_present_in_element(
#         (By.CLASS_NAME,'progress-label'),
#         "Complete!"
#     )
# )


WebDriverWait(driver,30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'progress-label'),
        "Complete!"
    )
)

