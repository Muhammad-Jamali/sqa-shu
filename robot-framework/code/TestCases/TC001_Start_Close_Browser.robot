*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${Broswer}  Chrome
${URL}  https://uibank.uipath.com/loans/apply

*** Test Cases ***
TC001 Browser Start and Close
    Open Browser  ${URL}  ${Broswer}
    Maximize Browser Window
    Enter Loan Form Values  gulraizgulshan@gmail.com  25000  3  600000  35 
    Sleep  3s

*** Keywords ***
Enter Loan Form Values
    [Arguments]  ${email}  ${amount}  ${term}  ${income}  ${age}
    Input Text  xpath://*[@id="email"]  ${email}
    Input Text  xpath://*[@id="amount"]  ${amount}
    Select From List By Value  xpath://*[@id="term"]  ${term}
    Input Text  //*[@id="income"]  ${income}
    Input Text  //*[@id="age"]  ${age}

