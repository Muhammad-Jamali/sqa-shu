*** Settings ***
Library    SeleniumLibrary
Resource   ../Resources/Resource4.robot
Test Setup    Start Broswer And Maximize
Test Teardown    Close Broswer Windows

*** Test Cases ***
TC_023 Setup And Teardown
    Set Selenium Speed    0.5 seconds
    Input Text    xpath://*[@id="email"]    gulraizgulshan@gmail.com
    Input Text    xpath://*[@id="amount"]    25000

    



    


