*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${broswer}  Chrome
${url}  https://uibank.uipath.com/loans/apply

*** Test Cases ***
TC_0016 Handle Multiple Browser Tabs
    Open Browser    ${url}    ${Broswer}    uibank_browser
    Maximize Browser Window

    


