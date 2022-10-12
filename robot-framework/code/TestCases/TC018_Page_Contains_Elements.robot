*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${broswer}  Chrome
${url}  https://uibank.uipath.com/loans/apply

*** Test Cases ***
TC_0018 Page Contains Elements
    Open Browser    ${url}    ${Broswer}    uibank_browser
    Maximize Browser Window
    Page Should Contain    Loan Application
    Click Element    xpath://a[contains(text(), 'Login')]
    Page Should Contain Textfield    xpath://*[@id="username"]
    Input Text    xpath://*[@id="username"]    gulraizgulshan

    ## Other usefull Keywords
    #Element Should ......

    


