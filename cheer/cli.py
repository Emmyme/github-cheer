from cheer.api import GithubAPI
from cheer.messages import get_message
from datetime import datetime, timedelta
from colorama import Fore, Style, init
import os

init(autoreset=True)

# Get credentials from environment variables or use defaults
USERNAME = os.getenv('GITHUB_USERNAME', "your-username")  # Default fallback
TOKEN = os.getenv('GITHUB_TOKEN', None)  # Optional token

api = GithubAPI(USERNAME, TOKEN)

try:
    events = api.get_events()
    
    # Calculate commits
    today = datetime.now().date()
    one_week_ago = today - timedelta(days=7)
    
    commits_today = sum(len(e['payload']['commits'])
                        for e in events
                        if e['type'] == 'PushEvent' and datetime.fromisoformat(e['created_at'][:-1]).date() == today)
    
    commits_week = sum(len(e['payload']['commits'])
                       for e in events
                       if e['type'] == 'PushEvent' and one_week_ago <= datetime.fromisoformat(e['created_at'][:-1]).date() <= today)
    
    # Print the message
    message = get_message(commits_today, commits_week)
    print(Fore.MAGENTA + message + Style.RESET_ALL)
    
except Exception as e:
    print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)
    print(Fore.YELLOW + "Make sure your GitHub username is correct and your repositories are public." + Style.RESET_ALL)
