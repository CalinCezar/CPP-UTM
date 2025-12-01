Feature: Add to Cart Functionality

  Background:
    Given I am on the Mens page

  Scenario: Verify Add to Cart button
    When I add the first product to the cart
    Then the cart item count should increase
    And the product should be in the cart
