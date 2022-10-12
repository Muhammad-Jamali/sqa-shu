*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${Broswer}  Chrome
${URL}  https://uibank.uipath.com/loans/apply

*** Test Cases ***
TC_0014 Wait Keyword Commands
    Open Browser    ${URL}    ${Broswer}
    Maximize Browser Window
    Wait Until Page Contains    Loan Application

    Input Text    xpath://*[@id="email"]    gulraizgulshan@gmail.com
    Input Text    xpath://*[@id="amount"]    25000
    Select From List By Value    //*[@id="term"]    1
    Input Text    xpath://*[@id="income"]    250000
    Input Text    xpath://*[@id="age"]    25

    Click Button    xpath://*[@id="submitButton"]

    #Wait Until Page Contains Element    //*[@id="loanHomePage"]
    Wait Until Element Contains    xpath://html/body/app-root/body/div/app-loan-result/div/div[2]/div/h1[1][text()=" Congrats! "]    Congrats! 