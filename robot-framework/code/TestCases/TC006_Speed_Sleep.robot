*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${Broswer}  Chrome
${URL}  https://uibank.uipath.com/loans/apply

*** Test Cases ***
TC_006 Speed And Sleep Test
    Open Browser    ${URL}    ${Broswer}
    Maximize Browser Window
    # At each step
    Set Selenium Speed    2 seconds

    Input Text    xpath://*[@id="email"]  gulraizgulshan@gmail.com
    Input Text    xpath://*[@id="amount"]  25000
    Select From List By Value    xpath://*[@id="term"]  1
    Input Text    //*[@id="income"]  60000
    Input Text    //*[@id="age"]  31
    
    # At particular step
    Sleep    3s
       
   

