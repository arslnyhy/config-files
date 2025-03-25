#!/bin/bash

# Store the original directory where the script was called from
ORIGINAL_DIR=$(pwd)

# Ask for the target directory path or use current directory if none provided
echo "Enter the full path to the git repository (leave empty to use current directory):"
read TARGET_DIR

# Use current directory if no input was provided
if [ -z "$TARGET_DIR" ]; then
    TARGET_DIR="$ORIGINAL_DIR"
fi

# Check if the target directory exists
if [ ! -d "$TARGET_DIR" ]; then
    echo "Error: Directory does not exist: $TARGET_DIR"
    exit 1
fi

# Navigate to the target directory
cd "$TARGET_DIR"

# Check if it's a git repository
if [ ! -d ".git" ]; then
    echo "Error: Not a git repository: $TARGET_DIR"
    exit 1
fi

# Set up the git hooks
git config core.hooksPath .githooks
mkdir -p .githooks
chmod +x .githooks/pre-commit 2>/dev/null || true

# Check if the hooks path is set correctly
if [ "$(git config --get core.hooksPath)" = ".githooks" ]; then
    echo "Successfully added the git hook to: $TARGET_DIR"
else
    echo "Failed to add the git hook to: $TARGET_DIR"
fi

# Return to the original directory
cd "$ORIGINAL_DIR"