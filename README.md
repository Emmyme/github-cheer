# GitHub Cheer

A fun and motivating tool that tracks your GitHub activity and provides encouraging messages based on your commit activity. Perfect for developers who want a little boost of motivation after pushing their code!

## Features

- **Activity Tracking**: Monitors your GitHub commits for today and the past week
- **Git Hooks Integration**: Automatically runs after every push with git hooks
- **Easy Setup**: Simple configuration with just your GitHub username (token optional)

## Installation

1. **Clone the repository**:

   ```bash
   git clone <your-repo-url>
   cd github-cheer
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your GitHub credentials**:

   **For local installation** - Edit `cheer/cli.py`:

   ```python
   USERNAME = "your-github-username"  # Change this to your GitHub username
   TOKEN = None  # Optional: Set to your token for authenticated requests
   ```

   **Or set environment variables** (recommended for global use):
   The script automatically checks for `GITHUB_USERNAME` and `GITHUB_TOKEN` environment variables first.

   **For global installation** - Set environment variables:

   **Unix/Linux/macOS:**

   ```bash
   # Add these lines to your shell profile (.bashrc, .zshrc, etc.)
   export GITHUB_USERNAME="your-github-username"
   export GITHUB_TOKEN="your-github-token"  # Optional

   # Then reload your profile:
   source ~/.bashrc  # or ~/.zshrc
   ```

   **Windows PowerShell:**

   ```powershell
   # Add these lines to your PowerShell profile
   $env:GITHUB_USERNAME = "your-github-username"
   $env:GITHUB_TOKEN = "your-github-token"  # Optional

   # Or set them for current session:
   $env:GITHUB_USERNAME = "your-github-username"
   $env:GITHUB_TOKEN = "your-github-token"
   ```

   > **Note**: The tool works with public GitHub data by default. If you want to access private repositories or have higher rate limits, you can create a GitHub Personal Access Token.

4. **Install git hooks** (optional):

   **Local installation** (for this repository only):

   ```bash
   chmod +x install-hooks.sh
   ./install-hooks.sh
   ```

   **Global installation** (for all repositories):

   ```bash
   # 1. Set up a global git hooks directory
   git config --global core.hooksPath ~/.git-hooks

   # 2. Create the global hooks directory
   mkdir ~/.git-hooks

   # 3. Copy the hook and cheer module to the global location
   cp hooks/post-commit ~/.git-hooks/
   cp -r cheer ~/.git-hooks/
   cp requirements.txt ~/.git-hooks/

   # 4. Install dependencies globally
   pip install -r ~/.git-hooks/requirements.txt
   ```

   **What this does:**

   - Sets up a global hooks directory that works for all repositories
   - Copies the GitHub Cheer tool to the global location
   - Installs required dependencies globally
   - The hook will now run after every commit in any repository

## Usage

### Manual Usage

Run the script directly to see your activity:

```bash
python cheer/cli.py
```

### Automatic Usage (with Git Hooks)

Once you've installed the git hooks, the script will automatically run after every `git commit`, showing you an encouraging message about your activity.

**Note**:

- **Local hooks** only work in this repository
- **Global hooks** work in all repositories after setup
- The tool tracks commits pushed to GitHub, not local commits

## How It Works

The tool fetches your public GitHub events and analyzes your commit activity:

- **Today's commits**: Counts all commits made today
- **Weekly commits**: Counts all commits made in the past 7 days

Based on your activity, you'll receive different encouraging messages:

- **High achiever**: 3+ commits today → "Wow! X commits today! Keep crushing it!"
- **Consistent coder**: 10+ commits this week → "You made X commits this week! You're on fire!"
- **Steady progress**: Default message → "Good job! You made X commits today and Y commits this week. Keep it up!"

## Project Structure

```
github-cheer/
├── cheer/
│   ├── __init__.py
│   ├── api.py          # GitHub API integration
│   ├── cli.py          # Command-line interface
│   └── messages.py     # Encouraging message logic
├── hooks/
│   └── post-push       # Git hook script
├── install-hooks.sh    # Hook installation script
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Dependencies

- `requests`: For GitHub API calls
- `colorama`: For colored terminal output

## Contributing

Feel free to contribute to this project! Some ideas:

- Add more message variations
- Support for different time periods
- Integration with other Git hosting platforms
- Web dashboard for activity visualization

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have questions, please open an issue on GitHub.

---

**Keep on coding!**
