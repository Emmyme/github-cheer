#!/bin/bash

if [ ! -d ".git" ]; then
    echo "Error: Not in a git repository. Please run this script from the root of your git repository."
    exit 1
fi

mkdir -p .git/hooks

cp hooks/post-commit .git/hooks/
chmod +x .git/hooks/post-commit

echo "Git hooks installed successfully!"
echo "The GitHub Cheer tool will now run automatically after every git commit."
echo ""
echo "Make sure to configure your GitHub credentials in cheer/cli.py or set environment variables."
