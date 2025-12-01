from behave import when, then
from pages.mens_page import MensPage
import time

@when('I click on the "{link_name}" link')
def step_impl(context, link_name):
    context.mens_page.click_nav_item(link_name)

@then('I should be redirected to the "{page_title}" page')
def step_impl(context, page_title):
    # Allow some time for navigation
    time.sleep(2)
    assert page_title in context.driver.title

@when('I scroll to the footer')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

@when('I click on the Contact link in the footer')
def step_impl(context):
    context.mens_page.click_footer_contact()

@then('I should be redirected to the Contact page or external link')
def step_impl(context):
    time.sleep(2)
    current_url = context.driver.current_url
    
    # Check for the bug (YouTube redirection)
    if "youtube.com" in current_url:
        assert False, f"Bug detected: Redirected to YouTube instead of Contact page. URL: {current_url}"
    
    # Check for expected behavior
    assert "contact" in current_url.lower() or "Contact" in context.driver.title, f"Not on Contact page. URL: {current_url}"
