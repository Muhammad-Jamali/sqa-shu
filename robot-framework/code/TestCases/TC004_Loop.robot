*** Settings ***
Library  SeleniumLibrary
Library  Collections

*** Test Cases ***
TC_004 List Test
    @{List1}    Create List    Hello  22  223.10  World  Abcd125

    FOR    ${i}    IN    @{List1}
        Log To Console   ${i}
        
    END

   

