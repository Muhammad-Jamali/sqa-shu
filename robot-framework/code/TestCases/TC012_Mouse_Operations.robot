*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${Broswer}  Chrome
${URL}  https://uibank.uipath.com/loans/apply

*** Test Cases ***
TC_0012 Mouse Operations
    Open Browser    ${URL}    ${Broswer}
    Maximize Browser Window

    Open Context Menu    xpath://*[@id="navbarDropdown"]

    

