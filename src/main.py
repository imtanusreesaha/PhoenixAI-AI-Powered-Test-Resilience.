import pytest
import sys
import os

def main():
    # Set up paths and configurations
    os.environ["ENV"] = "test"  # Set the environment if needed

    # Run the tests
    result = pytest.main(["tests/"])
    
    if result == 0:
        print("Tests executed successfully!")
    else:
        print("Tests failed. Check the logs for details.")

if __name__ == "__main__":
    main()
