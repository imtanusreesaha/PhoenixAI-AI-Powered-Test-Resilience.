import pytest
import allure
from selenium import webdriver
from src.self_healing import SelfHealingLocator

@allure.feature("Login Page")
@pytest.mark.parametrize("username,password", [("user1", "password1"), ("user2", "password2")])
def test_login(username, password):
    driver = webdriver.Chrome()
    driver.get("https://example.com/login")

    # Initialize self-healing locator
    shl = SelfHealingLocator(driver)

    # Locate elements dynamically with self-healing mechanism
    username_field = shl.find_element("username_field")
    password_field = shl.find_element("password_field")
    login_button = shl.find_element("login_button")

    # Interact with the page
    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()

    # Assertion to verify the test
    assert "Dashboard" in driver.title
    driver.quit()

@allure.feature("Checkout Page")
@pytest.mark.parametrize("item, quantity", [("Laptop", 1), ("Phone", 2)])
def test_checkout(item, quantity):
    driver = webdriver.Chrome()
    driver.get("https://example.com/checkout")

    shl = SelfHealingLocator(driver)

    checkout_button = shl.find_element("checkout_button")
    checkout_button.click()

    # Add assertions based on checkout logic
    assert "Order Summary" in driver.title
    driver.quit()
