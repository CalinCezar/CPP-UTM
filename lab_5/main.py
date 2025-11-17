from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

gecko_driver = os.getenv("gecko_driver")

options = Options()
options.binary_location = os.getenv("firefox_path")
service = Service(executable_path=gecko_driver)

driver = webdriver.Firefox(service=service, options=options)


driver.get("https://ebay.com")

search_box = WebDriverWait(driver, 15).until(
    EC.visibility_of_element_located((By.ID, "gh-ac"))
)
search_box.send_keys("computer")
search_box.send_keys(Keys.ENTER)

WebDriverWait(driver, 15).until(
    EC.visibility_of_element_located((By.ID, "gh-logo"))
)