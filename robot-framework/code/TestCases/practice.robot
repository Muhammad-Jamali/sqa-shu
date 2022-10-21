*** Settings ***
Library    SeleniumLibrary
Library    Collections

*** Variables ***
${FirstName}=    xpath://*[@id="firstName"]
${Title}=    xpath://*[@id="title"]
${MiddleName}=    xpath://*[@id="middleName"]
${LastName}=    xpath://*[@id="lastName"]
${Sex}=    xpath://*[@id="sex"]
${EmploymentStatus}=    xpath://*[@id="employmentStatus"]
${Age}=    xpath://*[@id="age"]
${MaritalStatus}=    xpath://*[@id="maritalStatus"]
${NumberOfDependents}=    xpath://*[@id="numberOfDependents"]
${Username}=    xpath://*[@id="username"]
${Email}=    xpath://*[@id="email"]
${Password}=    xpath://*[@id="password"]
${RegisterButton}=    xpath://button[@type="submit"]


*** Keywords ***
Start Browser And Maximize
    Open Browser    https://uibank.uipath.com/register-account    Chrome
Close Browser Window
    Close Browser

*** Test Cases ***
TC01 Check for the main heading of the form
    
    [Setup]  Start Browser And Maximize
    [Teardown]    Close Browser Window

    Maximize Browser Window
    Page Should Contain Element    xpath:/html/body/app-root/body/div/app-register/div/div[2]/h1    Register
    Log To Console    The page contains the heading "Register"

TC02 Check the availability of form fields

    [Setup]  Start Browser And Maximize
    [Teardown]    Close Browser Window

    Page Should Contain    First Name
    Page Should Contain    Title
    Page Should Contain    Middle Name Or Initial
    Page Should Contain    Last Name
    Page Should Contain    Sex
    Page Should Contain    Employment Status
    Page Should Contain    Age
    Page Should Contain    Marital Status
    Page Should Contain    Number of Dependents
    Page Should Contain    Username
    Page Should Contain    Email address
    Page Should Contain    Password
    Log To Console    The page contains 12 input fields

TC03 Check for the Placeholder of different form fields

    [Setup]  Start Browser And Maximize
    [Teardown]    Close Browser Window

    ${FirstName_Placeholder}=    Get Element Attribute    ${FirstName}    placeholder
    Log To Console    ${FirstName_Placeholder}
    Should Not Be Empty    ${FirstName_Placeholder}

    ${MiddleName_Placeholder}=    Get Element Attribute    ${MiddleName}    placeholder
    Log To Console    ${MiddleName_Placeholder}
    Should Not Be Empty    ${MiddleName_Placeholder}

    ${LastName_Placeholder}=    Get Element Attribute    ${LastName}    placeholder
    Log To Console    ${LastName_Placeholder}
    Should Not Be Empty    ${LastName_Placeholder}

    ${Age_Placeholder}=    Get Element Attribute    ${Age}    placeholder
    Log To Console    ${Age_Placeholder}
    Should Not Be Empty    ${Age_Placeholder}

    ${NumberOfDependents_Placeholder}=    Get Element Attribute    ${NumberOfDependents}    placeholder
    Log To Console    ${NumberOfDependents_Placeholder}
    Should Not Be Empty    ${NumberOfDependents_Placeholder}

    ${Username_Placeholder}=    Get Element Attribute    ${Username}    placeholder
    Log To Console    ${Username_Placeholder}
    Should Not Be Empty    ${Username_Placeholder}

    ${Email_Placeholder}=    Get Element Attribute    ${Email}    placeholder
    Log To Console    ${Email_Placeholder}
    Should Not Be Empty    ${Email_Placeholder}

    ${Password_Placeholder}=    Get Element Attribute    ${Password}    placeholder
    Log To Console    ${Password_Placeholder}
    Should Not Be Empty    ${Password_Placeholder}

TC04 Check the Title field for given list items
    
    [Setup]  Start Browser And Maximize
    [Teardown]    Close Browser Window

    @{Title_listItems}=    Get List Items    ${Title}
    Log To Console    ${Title_listItems}
    List Should Contain Value    ${Title_listItems}    Ms
    List Should Contain Value    ${Title_listItems}    Mrs
    List Should Contain Value    ${Title_listItems}    Mr

    
    @{Sex_listItems}=    Get List Items    ${Sex}
    Log To Console    ${Sex_listItems}
    List Should Contain Value    ${Sex_listItems}    Male
    List Should Contain Value    ${Sex_listItems}    Female

    ${EmploymentStatus_Tag}=    Get WebElement    ${EmploymentStatus}
    Log To Console    ${EmploymentStatus_Tag.tag_name}
    Should Be Equal As Strings    ${EmploymentStatus_Tag.tag_name}    select

    @{MaritalStatus_listItems}=    Get List Items    ${MaritalStatus}
    Log To Console    ${MaritalStatus_listItems}
    ${MaritalStatus_Items_Count}=    Get Length    ${MaritalStatus_listItems}
    Should Be Equal As Numbers    ${MaritalStatus_Items_Count}    4

    ${Email_Type}=    Get Element Attribute    ${Email}    type
    Should Be Equal As Strings    ${Email_Type}    email

    ${Password_Type}=    Get Element Attribute    ${Password}    type
    Should Be Equal As Strings    ${Password_Type}    password

    Input Text    ${FirstName}    Gulraeez
    Sleep    1s

    Select From List By Label    ${Title}    Mr
    Sleep    1s
    
    Input Text    ${MiddleName}    Engr.
    Sleep    1s
    
    Input Text    ${LastName}    Gulshan
    Sleep    1s

    Select From List By Label    ${Sex}    Male
    Sleep    1s

    Select From List By Label    ${EmploymentStatus}    Full-time
    Sleep    1s
    
    Input Text    ${Age}    01/10/90
    Sleep    1s

    Select From List By Label    ${MaritalStatus}    Married
    Sleep    1s
    
    Input Text    ${NumberOfDependents}    2
    Sleep    1s
    
    Input Text    ${Username}    gulraeezgulshan
    Sleep    1s
    
    Input Text    ${Email}    gulraeezgulshan@gmail.com
    Sleep    1s
    
    Input Password    ${Password}    123456
    Sleep    1s
    
    Click Button    ${RegisterButton}

    Wait Until Page Contains   Welcome To The UiBank Family!


