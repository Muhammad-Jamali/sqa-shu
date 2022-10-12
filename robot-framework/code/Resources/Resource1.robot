*** Settings ***
Library    SeleniumLibrary
Resource    Resource4.robot

*** Variables ***
${broswer}  Chrome
${url}  https://uibank.uipath.com/loans/apply

*** Keywords ***
Open and Maximize Broswer
    Log To Console    Opening Browser Now
    Open Browser    ${url}    ${Broswer}    uibank_browser
    Maximize Browser Window

Close Broswer
    Log To Console    Closing Browser Now
    Sleep    2 seconds
    Close Broswer Windows
