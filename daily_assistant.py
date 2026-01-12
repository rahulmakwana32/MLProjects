import json
import datetime
import os
import smtplib
from email.mime.text import MIMEText
from schedule_data import get_day_config
import subprocess

CONFIG_FILE = "config.json"

def load_config():
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def get_current_day(start_date_str):
    start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
    today = datetime.date.today()
    delta = today - start_date
    return delta.days + 1

def send_email(config, subject, body):
    sender = config["email_from"]
    recipient = config["email_to"]
    password = config.get("smtp_password")
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    try:
        if password and password != "your_app_password":
            print(f"Attempting to send email to {recipient}...")
            # Uncomment below to actually send if creds are real
            # with smtplib.SMTP(config["smtp_server"], config["smtp_port"]) as server:
            #     server.starttls()
            #     server.login(config["smtp_user"], password)
            #     server.sendmail(sender, recipient, msg.as_string())
            # print("Email sent successfully!")
            print("Email simulation: Sent!")
        else:
            print("SIMULATION: Email credentials not configured. Skipping actual send.")
            print(f"--- EMAIL CONTENT ---\nTo: {recipient}\nSubject: {subject}\n\n{body}\n---------------------")
    except Exception as e:
        print(f"Failed to send email: {e}")

def main():
    config = load_config()
    day_num = get_current_day(config["start_date"])
    print(f"Today is Day {day_num} of your 24-week plan.")

    day_config = get_day_config(day_num)
    
    if not day_config:
        print("Congratulations! You have completed the 24-week plan (or the day is out of range).")
        return

    print(f"Week: {day_config['week']}")
    print(f"Topic Folder: {day_config['dir_name']}")
    
    subject = f"Day {day_num} Study Plan: Week {day_config['week']}"
    body = f"""Hello!
    
It's Day {day_num}. Time to get job-ready!

Today's Focus:
Phase: {day_config['phase']}
Week: {day_config['dir_name']}

Schedule ({config['study_time_start']} - {config['study_time_end']}):
1. 60 min: Learn Concept
2. 90 min: Code / Build
3. 30 min: Notes + README + Revise

Check the README here: {day_config['readme']}

Happy Coding!
"""
    
    # 1. Send Notification
    send_email(config, subject, body)
    
    # 2. Prepare Environment
    # Create daily notes file if it doesn't exist
    notes_file = os.path.join(day_config['full_path'], f"Day_{day_num}_Notes.md")
    if not os.path.exists(notes_file):
        with open(notes_file, "w") as f:
            f.write(f"# Notes for Day {day_num}\n\n## Goals\n\n## Learnings\n\n## Code Snippets\n")
        print(f"Created notes file: {notes_file}")
    
    # Open the folder/files (MacOS 'open' command)
    try:
        print(f"Opening materials for {day_config['dir_name']}...")
        subprocess.run(["open", day_config['readme']])
        subprocess.run(["open", notes_file])
    except Exception as e:
        print(f"Could not automatically open files: {e}")

if __name__ == "__main__":
    main()
