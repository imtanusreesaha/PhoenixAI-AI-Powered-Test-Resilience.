import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from src.self_healing import SelfHealingLocator

# Adding the src directory to the system path for importing modules
import sys
import os
src_path = "/content/src"  # Adjust this path based on where your 'src' folder is located
sys.path.insert(0, src_path)


@allure.feature("Checkout Page")
@pytest.mark.parametrize("item, quantity", [("Laptop", 1), ("Phone", 2)])
def test_checkout(item, quantity):
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

    # Open the checkout page
    driver.get("https://example.com/checkout")

    # Print the page title to verify if the page loaded
    print("Page Title:", driver.title)

    # Take a screenshot to verify if the page was rendered correctly
    driver.save_screenshot('/content/screenshot.png')
    print("Screenshot saved as '/content/screenshot.png'")

    # Initialize self-healing locator
    shl = SelfHealingLocator(driver)

    # Dynamically locate the checkout button using self-healing locator
    checkout_button = shl.find_element("checkout_button")
    
    # Click the checkout button to proceed to the order summary
    checkout_button.click()

    # Add assertions to verify that the user is on the "Order Summary" page
    assert "Order Summary" in driver.title

    # Close the browser after the test
    driver.quit()
