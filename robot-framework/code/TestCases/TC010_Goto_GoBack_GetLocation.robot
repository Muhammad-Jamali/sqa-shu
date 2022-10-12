*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${Broswer}  Chrome
${URL}  https://uibank.uipath.com/loans/apply

*** Test Cases ***
TC_0010 Take Screenshot
    Open Browser    ${URL}    ${Broswer}    
    Go To    https://www.google.com

    ${url}=    Get Location
    Log To Console    ${url}

    Go Back    

    ${url}=    Get Location
    Log To Console    ${url}
    

