*** Settings ***
Library  SeleniumLibrary
Library  Collections

*** Test Cases ***
TC_005 Run Keyword Test
    ${Key_Var}=    Set Variable    Log To Console
    Run Keyword    ${Key_Var}    gulraizgulshan.com

    ${Var2}=    Set Variable    NO

    Run Keyword If    '${Var2}'=='YES'
    ...    Run Keyword    ${Key_Var}    gulraizgulshan.com
    ...  ELSE IF    '${Var2}'=='NO'
    ...    Run Keyword    ${Key_Var}    not found
   

