from behave import given, when, then
from pages.mens_page import MensPage

@given('I am on the Mens page')
def step_impl(context):
    context.mens_page = MensPage(context.driver)
    context.mens_page.load()

@then('the page title should contain "{text}"')
def step_impl(context, text):
    assert text in context.mens_page.get_title()
