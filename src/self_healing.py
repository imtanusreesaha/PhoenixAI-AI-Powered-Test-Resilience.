import json
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class SelfHealingLocator:
    def __init__(self, driver, locators_file="src/locators.json"):
        self.driver = driver
        self.locators = self.load_locators(locators_file)

    def load_locators(self, locators_file):
        """Load locators from a JSON file."""
        try:
            with open(locators_file, "r") as file:
                return json.load(file)
        except Exception as e:
            print(f"Error loading locators: {e}")
            return {}

    def find_element(self, name):
        """Tries different locator strategies and updates broken ones."""
        strategies = [By.ID, By.CLASS_NAME, By.XPATH, By.CSS_SELECTOR, By.NAME]

        for strategy in strategies:
            try:
                element = self.driver.find_element(strategy, self.locators[name])
                return element
            except NoSuchElementException:
                continue
        
        # If element is not found, attempt AI-based detection or auto-fix (future implementation)
        print(f"Element '{name}' not found using the available strategies.")
        return None
