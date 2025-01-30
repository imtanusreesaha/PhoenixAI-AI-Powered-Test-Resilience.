import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from src.self_healing import SelfHealingLocator

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

@allure.feature("Login Page")
@pytest.mark.parametrize("username, password", [("user1", "password1"), ("user2", "password2")])
def test_login(username, password):
    # Set Chrome options to run headlessly (without GUI)
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--remote-debugging-port=9222')

    # Path to chromedriver in Colab
    chromedriver_path = '/usr/lib/chromium-browser/chromedriver'

    # Set up the Service object
    service = Service(chromedriver_path)

    # Initialize WebDriver with the service object
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Open the login page
    driver.get("https://example.com/login")

    # Print the page title to verify if the page loaded
    print("Page Title:", driver.title)

    # Take a screenshot to verify if the page was rendered correctly
    driver.save_screenshot('/content/login_screenshot.png')
    print("Screenshot saved as '/content/login_screenshot.png'")

    # Initialize self-healing locator
    shl = SelfHealingLocator(driver)

    # Dynamically locate login form elements using self-healing locator
    username_field = shl.find_element("username_field")
    password_field = shl.find_element("password_field")
    login_button = shl.find_element("login_button")

    # Interact with the login page
    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()

    # Assertion to verify successful login
    assert "Dashboard" in driver.title

    # Close the browser after the test
    driver.quit()
