import imaplib
import email
import os
import json
from dotenv import load_dotenv
from email.header import decode_header, make_header

class EmailFetcher:
    """
    EmailFetcher is a class to fetch emails from a specified email address.
    It connects to the Gmail server using IMAP, searches for emails from a specific sender,
    and retrieves the email content.
    """
    def __init__(self, email_address: str, password: str = None) -> None:
        if not password:
            load_dotenv()
            self.password = password or os.getenv('EMAIL_PASSWORD')
        else:
            self.password = password
        self.email_address = email_address        
        self.mail = None

    def connect(self) -> None:
        self.mail = imaplib.IMAP4_SSL('imap.gmail.com')
        self.mail.login(self.email_address, self.password)
        self.mail.select('inbox')
    
    def disconnect(self) -> None:
        self.mail.logout()

    def _get_text_from_email(self, msg) -> bytes:
        for part in msg.walk():
            if part.get_content_type() == 'text/plain':
                return part.get_payload(decode=True)

    def load_existing_emails(self) -> list[dict]:
        if os.path.exists('emails.json'):
            with open('emails.json', 'r') as f:
                existing_emails = json.load(f)
        else:
            existing_emails = []
        return existing_emails

    def fetch_emails(self, sender_email: str) -> list[dict]:
        status, response = self.mail.search(None, f'FROM "{sender_email}"')
        email_ids = response[0].split()

        email_list = []

        existing_emails = self.load_existing_emails()
        existing_ids = {email['id'] for email in existing_emails}

        for email_id in email_ids:
            email_data = {}
            _, msg_data = self.mail.fetch(email_id, '(RFC822)')
            msg = email.message_from_bytes(msg_data[0][1])

            subject = str(make_header(decode_header(msg['Subject'])))
            email_data['from'] = msg['From']
            email_data['date'] = msg['date']
            email_data['id'] = msg['Message-ID']

            if email_data['id'] in existing_ids:
                continue

            body = self._get_text_from_email(msg)
            if body:
                email_data['body'] = body.decode()

            email_list.append(email_data)

        return email_list
