import imaplib
import email
from email.header import decode_header
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
IMAP_SERVER = os.getenv("IMAP_SERVER", "imap.gmail.com")

def get_inbox():
    # print({ "Email": EMAIL, "Password": PASSWORD })
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL, PASSWORD)
    print("Logged in to IMAP server.")
    mail.select("inbox")
    # mail.

    status, data = mail.search(None, "UNSEEN")
    mail_ids = data[0].split()

    messages = []
    for msg_id in mail_ids:
        status, msg_data = mail.fetch(msg_id, "(RFC822)")
        msg = email.message_from_bytes(msg_data[0][1])

        subject, encoding = decode_header(msg["Subject"])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding or "utf-8", errors="ignore")

        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body += part.get_payload(decode=True).decode("utf-8", errors="ignore")
        else:
            body = msg.get_payload(decode=True).decode("utf-8", errors="ignore")

        messages.append({
            "id": msg_id.decode(),
            "subject": subject,
            "body": body.strip()
        })

    mail.logout()
    return messages

