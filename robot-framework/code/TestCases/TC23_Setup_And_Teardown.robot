*** Settings ***
Library    SeleniumLibrary
Resource   ../Resources/Resource4.robot


*** Test Cases ***
TC_023 Setup And Teardown
    [Setup]    Start Broswer And Maximize
    [Teardown]    Close Broswer Windows
    Set Selenium Speed    0.5 seconds
    Input Text    xpath://*[@id="email"]    gulraizgulshan@gmail.com
    Input Text    xpath://*[@id="amount"]    25000
    Sleep    5 seconds

TC 100 New Test Cases
    Log To Console    Hello


    


