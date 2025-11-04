import imaplib
import os
from dotenv import load_dotenv

load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
IMAP_SERVER = os.getenv("IMAP_SERVER", "imap.gmail.com")

def mark_as_read(msg_id):
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL, PASSWORD)
    mail.select("inbox")
    mail.store(msg_id, '+FLAGS', '\\Seen')
    mail.logout()
