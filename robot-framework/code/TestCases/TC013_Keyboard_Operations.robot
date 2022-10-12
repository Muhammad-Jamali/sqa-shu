*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${Broswer}  Chrome
${URL}  https://uibank.uipath.com/loans/apply

*** Test Cases ***
TC_0013 Keyboard Operations
    Open Browser    ${URL}    ${Broswer}
    Maximize Browser Window

    Click Link    xpath:/html/body/app-root/body/app-nav-menu/header/nav/div/div/ul/li[2]/a
    Press Keys    //*[@id="username"]    gulraizgulshan@gmail.com    

