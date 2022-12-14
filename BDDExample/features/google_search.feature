@sanity
Feature: Search feature
  Background:
    Given I navigate to google.com
    #after_step

   # before_scenario
  Scenario: Validating the search feature
    When I validate the page title
    #after_step
    Then I enter the text as "Hello Selenium"
    #after_step
    And I click the search button
    #after_step
    #after_scenario

    #before_scenario
  Scenario: Validating the search feature with new text
    When I validate the page title
    #after_step
    Then I enter the text as "Hello Behave"
    #after_step
    And I click the search button
    #after_step
    #after_scenario