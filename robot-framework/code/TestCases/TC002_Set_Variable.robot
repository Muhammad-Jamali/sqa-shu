*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
TC_002 Vairable Test
    ${var1}=  Set Variable  HelloWorld
    Log To Console  ${var1}

