from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest

def get_data():
    return [
        ("abc@gmail.com", "111111"),
        ("def@gmail.com", "222222"),
        ("ghi@gmail.com", "333333")
    ]

def setup_function():
    global driver
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://uibank.uipath.com/")
    driver.maximize_window()

def teardown_functin():
    driver.quit()

@pytest.mark.parametrize("username,password", get_data())
def test_dologin(username, password):
    print(username, "---", password)
    driver.find_element(By.ID,"username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)


#For paralell testing
#pip install pytest-html
#pytest .\test_8_html_reports.py --html=testreports.html
#pytest --html=testreports.html
