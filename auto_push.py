import os
import subprocess
from datetime import datetime

# Base path: Data_Wrangling repo
BASE_PATH = "."

# Change working directory to repo
os.chdir(BASE_PATH)

# Function to run git commands
def git(cmd):
    result = subprocess.run(["git"] + cmd, capture_output=True, text=True)
    return result.stdout.strip()

# Step 1: Check git status
status = git(["status", "--porcelain"])

if not status:
    print("✅ Nothing to commit. Repo is up-to-date.")
else:
    print("⚡ Changes detected. Preparing to push...")

    # Step 2: Add all changes
    git(["add", "."])
    print("➕ All changes staged.")

    # Step 3: Commit with timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    commit_msg = f"Auto-commit: {timestamp}"
    git(["commit", "-m", commit_msg])
    print(f"💾 Changes committed: '{commit_msg}'")

    # Step 4: Push to GitHub
    push_output = git(["push", "origin", "main"])
    print("🚀 Pushed to GitHub:\n", push_output)