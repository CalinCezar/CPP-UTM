from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options

def before_all(context):
    # Setup Firefox options
    firefox_options = Options()
    # firefox_options.add_argument("--headless") # Uncomment if you want headless mode

    # Initialize WebDriver
    # Using webdriver_manager to automatically handle driver installation
    service = Service(GeckoDriverManager().install())
    context.driver = webdriver.Firefox(service=service, options=firefox_options)
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)

def after_all(context):
    if hasattr(context, 'driver'):
        context.driver.quit()

def before_scenario(context, scenario):
    # Clear cookies or reset state if needed
    context.driver.delete_all_cookies()
