# Line Notifier GitHub Action

This project sets up a GitHub Action that sends notifications to a Line chat using Line Notify. It's scheduled to run automatically and can also be triggered manually.

## Prerequisites

1. A GitHub account
2. A Line account
3. Line Notify set up in your desired Line chat or group

## Setup Instructions

### 1. Line Notify Token

1. Go to [Line Notify](https://notify-bot.line.me/)
2. Log in and click on "Generate token"
3. Choose the chat you want to send notifications to (e.g., a group chat)
4. Name your token and generate it
5. Copy the token - you'll need it for the next step in python script
6. Add Line Notify Bot to your Line chat

### 2. GitHub Repository Setup

1. Create a new repository or use an existing one
2. Go to your repository's settings
3. Click on "Secrets and variables" then "Actions"
4. Click "New repository secret"
5. Name: `LINE_NOTIFY_TOKEN`, Value: [Your Line Notify Token]

### 3. Workflow File

Create a file named `.github/workflows/line_notify.yml` in your repository with the following content:

```yaml
name: Weekly Line Notifier

on:
  schedule:
    - cron: '00 6 * * 5'  # Runs every Friday at 14:00 UTC-8, because of github action time zone is UTC
  workflow_dispatch:  # Allows manual triggering

jobs:
  send_notification:
    runs-on: ubuntu-latest
    steps:
    - name: Check out repository
      uses: actions/checkout@v2
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install requests python-dotenv
    
    - name: Send Line notification
      env:
        LINE_NOTIFY_TOKEN: ${{ secrets.LINE_NOTIFY_TOKEN }} # Set the LINE_NOTIFY_TOKEN environment variable in GitHub Secrets
      run: python notify.py
```

### 4. Python Script

Create a file named `notify.py` in the root of your repository with the content you want to send.

## Usage

### Automatic Runs

The action will run automatically every Friday at 14:00 UTC-8, sending a notification to your specified Line chat.

### Manual Triggering

1. Go to your repository on GitHub
2. Click on the "Actions" tab
3. Select the "Weekly Line Notifier" workflow
4. Click "Run workflow"
5. Click "Run workflow" in the popup

## Customization

- To change the schedule, modify the `cron` expression in the `line_notify.yaml` file
- To customize the message, edit the `message` string in the `notify.py` file