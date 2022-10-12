*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${Broswer}  Chrome
${URL}  https://uibank.uipath.com/loans/apply

*** Test Cases ***
TC_008 Implicit Wait
    Open Browser    ${URL}    ${Broswer}
    Maximize Browser Window

    Set Selenium Implicit Wait    20 seconds

    # Deliberatively given wrong locator
    # By default, It will wait for 0 seconds and immediately throw error
    Input Text    xpath://*[@id="email1"]  gulraizgulshan@gmail.com
    Input Text    xpath://*[@id="amount"]  25000
    Select From List By Value    xpath://*[@id="term"]  1
    Input Text    //*[@id="income"]  60000
    Input Text    //*[@id="age"]  31

   

