import requests

class GithubAPI:
    def __init__(self, username, token=None):
        self.username = username
        self.token = token
        # Use authenticated endpoint if token is available, otherwise public only
        if self.token:
            self.base_url = f"https://api.github.com/users/{username}/events"
        else:
            self.base_url = f"https://api.github.com/users/{username}/events/public"

    def get_events(self):
        if self.token:
            # Use authenticated request if token is provided
            response = requests.get(self.base_url, auth=(self.username, self.token))
        else:
            # Use public API without authentication
            response = requests.get(self.base_url)
        
        response.raise_for_status()
        return response.json()