*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${Broswer}  Chrome
${URL}  https://uibank.uipath.com/loans/apply

*** Test Cases ***
TC_0011 Execute Javascript
    Open Browser    ${URL}    ${Broswer}
    Maximize Browser Window

    Execute Javascript    window.scrollTo(0,1000)
    Sleep    10 seconds

    

