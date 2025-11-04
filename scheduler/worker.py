import time
import requests
from mail_api.imap_service import get_inbox
from mail_api.mail_actions import mark_as_read

MODEL_API_URL = "http://127.0.0.1:8000/predict"


def process_emails():
    emails = get_inbox()
    print(f"Fetched {len(emails)} emails.")

    for email_msg in emails:
        text = f"{email_msg['subject']} {email_msg['body']}"
        try:
            resp = requests.post(MODEL_API_URL, json={"text": text}, timeout=10).json()
        except Exception as e:
            print(f"Model API request failed: {e}")
            continue

        if resp.get("label") == "spam":
            mark_as_read(email_msg["id"])
            print(f"Marked spam email as read: {email_msg['subject']}")
        else:
            print(f"Not spam: {email_msg['subject']}")


def run_scheduler():
    SLEEP_SECONDS = 6 * 2

    while True:
        process_emails()
        print(f"Sleeping for {SLEEP_SECONDS} seconds...")
        time.sleep(SLEEP_SECONDS)
