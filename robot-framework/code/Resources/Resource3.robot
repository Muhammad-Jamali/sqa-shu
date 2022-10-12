*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Start Broswer And Maximize
    [Arguments]    ${url}    ${Broswer} 
    
    Open Browser    ${url}    ${Broswer}
    
    Maximize Browser Window
    
    ${title}=    Get Title
    
    [Return]    ${title}
