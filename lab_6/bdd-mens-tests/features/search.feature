Feature: Search Functionality

  Background:
    Given I am on the Mens page

  Scenario: Search for an existing product (Positive)
    When I search for "shirt"
    Then I should see results related to "shirt"

  Scenario: Search for a non-existing product (Negative)
    When I search for "noproduct"
    Then I should see a "No products found" message or appropriate feedback
