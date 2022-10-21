*** Settings ***
Library  SeleniumLibrary
Library  Collections

*** Test Cases ***
TC_003 List Test
    @{List1}  Create List  Hello  22  223.10  World  Abcd125
    ${List_Length}  Get Length  ${List1}
    Log To Console  ${List_Length}
    ${List_Data}  Get From List  ${List1}  1
    Log To Console  ${List_Data}


