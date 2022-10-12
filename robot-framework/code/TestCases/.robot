*** Settings ***
Library    SeleniumLibrary
Resource   ../Resources/Resource3.robot 

*** Test Cases ***
TC_020 User Defined Keywords With Arguements & Return
    ${Title}=    Start Broswer And Maximize    https://uibank.uipath.com/loans/apply    Chrome
    Input Text    xpath://*[@id="email"]    ${Title}



    


