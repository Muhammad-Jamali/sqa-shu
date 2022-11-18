from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(10)
driver.get('https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2022-23-1298134/points-table-standings')
driver.maximize_window()


rows = driver.find_elements(By.XPATH, "//body[1]/div[1]/section[1]/section[1]/div[5]/div[1]/div[3]/div[1]/div[8]/table[1]/tbody[1]/tr[@class='ds-text-tight-s']")
total_rows = len(rows)

cols = driver.find_elements(By.XPATH, "//body[1]/div[1]/section[1]/section[1]/div[5]/div[1]/div[3]/div[1]/div[8]/table[1]/tbody[1]/tr[@class='ds-text-tight-s'][1]/td")
total_cols = len(cols)

print("Rows: " , total_rows, "Columns: ", total_cols)

sleep(10)

for row in rows:
    print(row.text)

## Different Way ##

#//body[1]/div[1]/section[1]/section[1]/div[5]/div[1]/div[3]/div[1]/div[8]/table[1]/tbody[1]/tr[@class='ds-text-tight-s'][1]/td[2]

start_xpath = "//body[1]/div[1]/section[1]/section[1]/div[5]/div[1]/div[3]/div[1]/div[8]/table[1]/tbody[1]/tr[@class='ds-text-tight-s']["
mid_xpath = "]/td["
end_xpath = "]"

for row in range(1, total_rows+1):
    for col in range(1, total_cols+1):
        xpath = start_xpath + str(row) + mid_xpath + str(col) + end_xpath
        element = driver.find_element(By.XPATH, xpath)
        print(element.text)
    print()


