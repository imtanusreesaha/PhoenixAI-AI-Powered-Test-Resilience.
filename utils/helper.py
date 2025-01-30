# utils/helper.py

import yaml
import time

def read_yaml_config(config_file="config/config.yaml"):
    """Read and return the content of the YAML config file."""
    with open(config_file, "r") as file:
        return yaml.safe_load(file)

def retry(func, retries=3, delay=2):
    """Retries a function on failure."""
    for attempt in range(retries):
        try:
            return func()
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                raise e
