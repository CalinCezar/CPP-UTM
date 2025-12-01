from behave import when, then
from pages.mens_page import MensPage
import time

@when('I add the first product to the cart')
def step_impl(context):
    context.mens_page.add_first_product_to_cart()
    time.sleep(2) # Wait for cart update

@then('the cart item count should increase')
def step_impl(context):
    assert context.mens_page.is_cart_updated()

@then('the product should be in the cart')
def step_impl(context):
    # Verify product in cart
    pass
