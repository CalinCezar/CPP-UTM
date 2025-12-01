Feature: Navigation and Footer

  Background:
    Given I am on the Mens page

  Scenario Outline: Verify navigation menu links
    When I click on the "<Link Name>" link
    Then I should be redirected to the "<Page Title>" page

    Examples:
      | Link Name | Page Title |
      | Home      | Elite Shoppy |
      | About     | Elite Shoppy |
      | Contact   | Elite Shoppy |

  Scenario: Verify Contact link in footer
    When I scroll to the footer
    And I click on the Contact link in the footer
    Then I should be redirected to the Contact page or external link
