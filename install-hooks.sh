#!/bin/bash

# Copy the post-commit hook to .git/hooks/
cp hooks/post-commit .git/hooks/
chmod +x .git/hooks/post-commit

echo "Git hooks installed successfully!"
echo "The cheer tool will now run automatically after every git commit."
