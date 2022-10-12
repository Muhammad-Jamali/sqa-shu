*** Settings ***
Library    SeleniumLibrary
Resource   ../Resources/Resource2.robot 

*** Test Cases ***
TC_020 User Defined Keywords With Arguements
    Start Broswer And Maximize    https://uibank.uipath.com/loans/apply    Chrome
    Input Text    xpath://*[@id="email"]    gulraizgulshan@gmail.com



    


