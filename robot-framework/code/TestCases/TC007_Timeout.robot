*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${Broswer}  Chrome
${URL}  https://uibank.uipath.com/loans/apply

*** Test Cases ***
TC_007 Timeout Test
    Open Browser    ${URL}    ${Broswer}
    Maximize Browser Window

    ${default_timeout}=    Get Selenium Timeout

    Log To Console    ${default_timeout}

    # #Timeout changed to 20 seconds
    Set Selenium Timeout    20 seconds

    # #It will wait for 5sec to check for Testing
    
    # It will check inner text of element
    Wait Until Element Contains    xpath:/html/body/app-root/body/div/app-loan-application/div/div[2]/form/div[1]/label    Email Address of Requester
    #Wait Until Page Contains    Testing

    Input Text    xpath://*[@id="email"]  gulraizgulshan@gmail.com
    Input Text    xpath://*[@id="amount"]  25000
    Select From List By Value    xpath://*[@id="term"]  1
    Input Text    //*[@id="income"]  60000
    Input Text    //*[@id="age"]  31
    
    # # At particular step
    Sleep    3s
       
   

