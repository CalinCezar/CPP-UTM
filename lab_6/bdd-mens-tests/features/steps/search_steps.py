from behave import when, then
from pages.mens_page import MensPage

@when('I search for "{term}"')
def step_impl(context, term):
    context.mens_page.search_product(term)

@then('I should see results related to "{term}"')
def step_impl(context, term):
    # Check if we are on a 404 page or if no products are found
    title = context.driver.title
    if "Page not Found" in title or "404" in title:
        assert False, f"Search failed: Redirected to {title}"
    
    # Check for products
    try:
        products = context.mens_page.get_all_products()
        assert len(products) > 0, "No products found for valid search term"
    except:
        assert False, "Could not find product list or page crashed"

@then('I should see a "No products found" message or appropriate feedback')
def step_impl(context):
    # Check for specific message
    try:
        # Using the locator defined in MensPage, but accessing driver directly for simplicity in step if needed
        # or better, add a method in MensPage. For now, let's try to find the element.
        from selenium.webdriver.common.by import By
        msg_element = context.driver.find_element(By.XPATH, "//*[contains(text(), 'No products found')]")
        assert msg_element.is_displayed()
    except:
        assert False, "Expected 'No products found' message, but it was not visible (or page crashed)."
