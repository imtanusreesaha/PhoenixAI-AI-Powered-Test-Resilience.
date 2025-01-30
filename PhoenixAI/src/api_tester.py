import requests
import json

class APITester:
    def __init__(self, base_url):
        self.base_url = base_url

    def send_get_request(self, endpoint, params=None):
        """Send a GET request to an API endpoint."""
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, params=params)
        return self.handle_response(response)

    def send_post_request(self, endpoint, data):
        """Send a POST request to an API endpoint."""
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})
        return self.handle_response(response)

    def handle_response(self, response):
        """Handle the response from an API call."""
        if response.status_code == 200:
            return response.json()  # Return JSON response if status code is 200
        else:
            print(f"API call failed with status code {response.status_code}")
            return None
