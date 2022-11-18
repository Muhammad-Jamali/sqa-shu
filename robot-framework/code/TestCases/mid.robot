*** Settings ***
Library    SeleniumLibrary
Library    Collections
Library    XML

*** Variables ***
${Heading}=    xpath:/html/body/app-root/body/div/app-register/div/div[2]/h1

${FirstName}=    xpath://*[@id="firstName"]
${MiddleName}=    xpath://*[@id="middleName"]
${Title}=    xpath://*[@id="title"]
${EmploymentStatus}=    xpath://*[@id="employmentStatus"]
${MaritalStatus}=    xpath://*[@id="maritalStatus"]

*** Keywords ***
Open UiBank Browser
    Open Browser    https://uibank.uipath.com/register-account    chrome
Close UiBank Bank Browser
    Close Browser

*** Test Cases ***

TC001 Check for the main heading of the form
    [Setup]    Open UiBank Browser
    [Teardown]    Close UiBank Bank Browser
    
    Element Text Should Be    ${Heading}    Register

TC002 Check the availability of form input fields
    [Setup]    Open UiBank Browser
    [Teardown]    Close UiBank Bank Browser

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

TC003 Check the Placeholder of different input fields
    [Setup]    Open UiBank Browser
    [Teardown]    Close UiBank Bank Browser

    ${FirstNamePlaceholder}=    Get Element Attribute    ${FirstName}    placeholder
    Should Not Be Empty    ${FirstNamePlaceholder}

    ${MiddleNamePlaceholder}=    Get Element Attribute    ${MiddleName}    placeholder
    Should Not Be Empty    ${MiddleNamePlaceholder}
    
    Element Attribute Value Should Be    ${FirstName}    placeholder    Enter first name
    Element Attribute Value Should Be    ${MiddleName}    placeholder    Enter middle name or initial

TC004 Check the Title field for given list items
    
    [Setup]    Open UiBank Browser
    [Teardown]    Close UiBank Bank Browser

    ${TitleListItems}=    Get List Items    ${Title}

    List Should Contain Value    ${TitleListItems}    Ms
    List Should Contain Value    ${TitleListItems}    Mrs
    List Should Contain Value    ${TitleListItems}    Mr

TC006 Check the Employment Status Field
    [Setup]    Open UiBank Browser
    [Teardown]    Close UiBank Bank Browser
    
    ${EmploymentStatusElement}=    Get WebElement    ${EmploymentStatus}
    Log To Console    ${EmploymentStatusElement.tag_name}
    Should Be Equal    ${EmploymentStatusElement}    select 
TC007 Check the Marital Status Field
    [Setup]    Open UiBank Browser
    [Teardown]    Close UiBank Bank Browser

    ${MaritalStatusListItems}=    Get List Items    ${MaritalStatus}
    ${MaritalStatusLength}=    Get Length    ${MaritalStatusListItems}
    Should Be Equal As Numbers    ${MaritalStatusLength}    4



