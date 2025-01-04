#Here's a tag. To run it in the command line give --tags=smoke
@smoke_test
Feature: Search Feature
  Scenario Outline: Validating the search feature
    Given I navigate to google.com
    When I validate the page title
    Then I enter the text as "<search_title>"
    And I click the search button
#    Here a scenario outline where we give two different arguments to the parameter "<search_title>"
    Examples:
      | search_title |
      | Hello BDD |
      | Hello TDD |