from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import allure

@pytest.fixture()
def log_on_failure(request,get_browser):
    yield
    item = request.node
    driver = get_browser
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="dologin", attachment_type=AttachmentType.PNG)

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

@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.parametrize("username,password", get_data())
def test_dologin(username, password):
    print(username, "---", password)
    driver.find_element(By.ID,"username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    assert 1 == 2




