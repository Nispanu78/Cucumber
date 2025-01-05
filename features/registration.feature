Feature: Registration Feature
  Scenario Outline: Validating the Registration Feature
    Given I navigate to qa.way2automation.com
    When I enter the name as "<name>"
    Then I enter the phone number as "<Phone number>"
    And I enter the email as "<email>"
    And I enter the country as "<country>"
    And I enter the city as "<city>"
    And I enter the username as "<username>"
    And I enter the password as "<password>"
    And I click on the submit button
    Examples:
      | name        | Phone number | email               | country | city   | username  | password  |
      | Test User1  | 9711111558   | testuser1@test.com  | Poland  | Warsaw | testuser1 | test1234  |
      | Test User2  | 2134543456   | testuser2@test.com  | Germany | Berlin | testuser2 | test123456|