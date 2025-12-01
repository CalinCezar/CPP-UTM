Feature: Mens Page Functionality

  Background:
    Given I am on the Mens page

  Scenario: Verify Mens page loads correctly
    Then the page title should contain "Men's"
    And the main navigation menu should be visible
    And the footer should be visible

  Scenario: Verify products are displayed correctly
    Then I should see a list of products
    And each product should have an image, title, and price

  Scenario: Verify product details using Data Table (Bonus)
    Then I should see the following products:
      | Product Name        | Price   |
      | Party Men's Blazer  | $260.99 |
      | Analog Watch        | $160.99 |
      | Running Shoes       | $80.99  |
      | Formal Blue Shirt   | $45.99  |

  Scenario: Verify page responsiveness
    When I resize the browser to mobile size
    Then the menu should be collapsible or visible
    And the products should be displayed in a column
