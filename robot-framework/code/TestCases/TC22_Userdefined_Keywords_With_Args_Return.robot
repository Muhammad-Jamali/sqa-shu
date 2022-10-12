*** Settings ***
Library    SeleniumLibrary
Resource    ../Resources/Resource4.robot

*** Test Cases ***
TC_022 User Defined Keywords With Arguements & Return
    # [Documentation]    This is sample Documentation
    # [Timeout]    50s
    ${Title}=    Start Broswer And Maximize    https://uibank.uipath.com/loans/apply    Chrome
    Input Text    xpath://*[@id="email"]    ${Title}
    Close Broswer Windows



    


