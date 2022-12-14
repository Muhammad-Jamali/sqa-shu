import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@given(u'I navigate to google.com')
def step_impl(context):
    context.driver.get("http://google.com")
    context.driver.implicitly_wait(5)


@when(u'I validate the page title')
def step_impl(context):
    title = context.driver.title
    print("Title is " + title)
    assert "Poogle" in title


#I enter the text as "Hello Selenium"
@then(u'I enter the text as "{searchText}"')
def step_impl(context,searchText):
    context.driver.find_element(By.NAME,"q").send_keys(searchText)


@then(u'I click the search button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/form[1]/div[1]/div[1]/div[4]/center[1]/input[1]").click()
    time.sleep(3)


#behave features --tags=smoke
#behave features
#behave -f allure_behave.formatter:AllureFormatter -o allure_reports ./features --tags=smoke
#allure serve allure_reports
