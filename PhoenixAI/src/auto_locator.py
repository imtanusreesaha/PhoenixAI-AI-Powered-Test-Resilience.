from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
import json
import time

class AutoLocator:
    def __init__(self, driver: WebDriver, locators_file="src/locators.json"):
        self.driver = driver
        self.locators_file = locators_file
        self.locators = self.load_locators()

    def load_locators(self):
        """Load locators from the JSON configuration."""
        try:
            with open(self.locators_file, "r") as file:
                return json.load(file)
        except Exception as e:
            print(f"Failed to load locators: {e}")
            return {}

    def find_element(self, element_name):
        """Find element with self-healing mechanism."""
        locators = self.locators.get(element_name)
        if locators is None:
            print(f"No locators found for element '{element_name}'")
            return None

        strategies = [By.ID, By.CLASS_NAME, By.NAME, By.XPATH, By.CSS_SELECTOR]
        
        for strategy in strategies:
            try:
                return self.driver.find_element(strategy, locators[strategy])
            except Exception as e:
                print(f"Failed to find element using {strategy}: {e}")

        print(f"Element '{element_name}' could not be found using available strategies.")
        return None
