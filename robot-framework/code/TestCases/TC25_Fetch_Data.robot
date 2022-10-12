*** Settings ***
Library    SeleniumLibrary
Resource   ../Resources/Resource4.robot
Test Setup    Start Broswer And Maximize
Test Teardown    Close Broswer Windows

*** Test Cases ***
TC_25 Fetch Data
    Set Selenium Speed    0.5 seconds
    Input Text    xpath://*[@id="email"]    gulraizgulshan@gmail.com
    Input Text    xpath://*[@id="amount"]    25000
    Select From List By Value    xpath://*[@id="term"]    3

    ${Email}=    Get Value    xpath://*[@id="email"]
    ${Amount}=    Get Value    xpath://*[@id="amount"]
    ${LoanTerm}=    Get Selected List Label    xpath://*[@id="term"]
    ${ButtonText}=    Get Text    xpath://*[@id="submitButton"]
    ${SeleniumSpeed}=    Get Selenium Speed
    ${URL}=    Get Location

    Log To Console    ${Email} ${Amount} ${LoanTerm} ${ButtonText} ${SeleniumSpeed}
    
    



    


