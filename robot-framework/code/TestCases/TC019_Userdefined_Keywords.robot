*** Settings ***
Library    SeleniumLibrary
Resource   ../Resources/Resource1.robot

*** Test Cases ***
TC_0019 User Defined Keywords
    Open and Maximize Broswer
    Input Text    xpath://*[@id="email"]    gulraizgulshan@gmail.com
    Close Broswer



    


