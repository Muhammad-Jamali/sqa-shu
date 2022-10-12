*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${Broswer}  Chrome
${URL}  https://uibank.uipath.com/loans/apply

*** Test Cases ***
TC_009 Take Screenshot
    Open Browser    ${URL}    ${Broswer}    
    Maximize Browser Window
    Input Text    xpath://*[@id="email"]  gulraizgulshan@gmail.com
    Input Text    xpath://*[@id="amount"]  25000
    Select From List By Value    xpath://*[@id="term"]  1
    Input Text    //*[@id="income"]  60000
    Input Text    //*[@id="age"]  31

    # Use forward slash while giving path
    Capture Page Screenshot    D:/salim-habib-university/software-quality-assurance/robot-framework/code/TC009.png
    
    #It will close all the browsers opened by script while keeping others browser open
    Close All Browsers

