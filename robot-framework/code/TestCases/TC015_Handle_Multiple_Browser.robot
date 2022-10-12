*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${broswer}  Chrome
${url1}  https://uibank.uipath.com/loans/apply
${url2}  https://www.google.com

*** Test Cases ***
TC_0015 Handle Multiple Browser
    Open Browser    ${url1}    ${Broswer}    uibank_browser
    Maximize Browser Window
    Open Browser    ${url2}    ${Broswer}    google_browser
    Maximize Browser Window

    #Switch Browser    1
    Switch Browser    uibank_browser
    ${var1}=    Get Location
    Log To Console    ${var1}

    #Switch Browser    2
    Switch Browser    google_browser
    ${var2}=    Get Location
    Log To Console    ${var2}

    Input Text    xpath://input[@name="q"]    Salim Habib University
    Press Keys    xpath://input[@name="q"]    RETURN
    


