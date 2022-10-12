*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${broswer}  Chrome
${url}  https://uibank.uipath.com/loans/apply

*** Test Cases ***
TC_0017 Page Contains Text
    Open Browser    ${url}    ${Broswer}    uibank_browser
    Maximize Browser Window
    Page Should Contain    Loan Application
    Click Element    xpath://a[contains(text(), 'Login')]

    


