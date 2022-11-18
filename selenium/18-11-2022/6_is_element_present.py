from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep


# def is_element_present(how,what):
#     try:
#         driver.find_element(by=how, value=what)
#         return True
#     except:
#         return False

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.maximize_window()

def is_element_present(how,what):
    if(len(driver.find_elements(by=how, value=what))== 0):
        return False
    else:
        return True

driver.get('https://www.wikipedia.org/')


#print(is_element_present(By.ID, "searchLanguage"))
print(is_element_present(By.ID, "dfsdfsdfs"))



