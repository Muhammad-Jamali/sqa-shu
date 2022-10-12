*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${broswer}  Chrome
${url}  https://uibank.uipath.com/loans/apply

*** Keywords ***
Start Broswer And Maximize
    Open Browser    ${url}    ${Broswer}    uibank_browser
    Maximize Browser Window

Close Broswer Windows
    Log To Console    "Closing Broswer"
    Close Browser

