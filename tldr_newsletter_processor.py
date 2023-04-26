import os
import json
from dotenv import load_dotenv
from email_fetcher import EmailFetcher
from email_parser import TLDRParser
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
import logging

from tldr_few_shot import system_message, example_in, example_out
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()  # Load environment variables from the .env file

class TLDRNewsletterProcessor:
    """
    TLDRNewsletterProcessor is a class to process the TLDR Newsletter emails.
    It fetches emails, parses them into sections, and processes the content
    with a chat model.
    """
    def __init__(self, user_email: str, newsletter_email: str = 'dan@tldrnewsletter.com') -> None:
        self.user_email = user_email
        self.newsletter_email = newsletter_email
        self.email_fetcher = EmailFetcher(self.user_email)
        self.parser = TLDRParser()
        self.chat = ChatOpenAI(temperature=.4, max_retries=0, max_tokens=2400)
        self.messages = [
            SystemMessage(content=system_message),
            HumanMessage(content=example_in),
            AIMessage(content=example_out)
        ]

    def fetch_emails(self) -> list[dict]:
        self.email_fetcher.connect()
        emails_d = self.email_fetcher.fetch_emails(self.newsletter_email)
        self.email_fetcher.disconnect()
        logging.info(f"Fetched {len(emails_d)} emails")
        return emails_d
        
    def process_emails(self, emails: list[dict]) -> None:
        logging.info("Processing emails...")
        data_dir = os.path.abspath(os.path.join(os.getcwd(), 'data'))
        if not os.path.exists(data_dir):
            os.mkdir(data_dir)

        output_json = os.path.join(data_dir, 'tldr_records.json')
        error_file = os.path.join(data_dir, 'error_records.json')

        for email_obj in emails:
            if 'body' in email_obj:
                parts = self.parser.parse(email_obj['body'])
                for part in parts:
                    if not part:
                        logging.info("Empty record. Skipping.")
                        continue
                    to_run = self.messages.copy()
                    to_run.append(HumanMessage(content=part))

                    success = False
                    retries = 3
                    while not success and retries > 0:
                        try:
                            results = self.chat(to_run)
                            obj = eval(results.content)
                            success = True
                        except Exception as e:
                            retries -= 1
                            logging.warning(f"Processing failed, retries left: {retries}. Exception: {e}")

                    if success:
                        logging.info("Processing successful")
                        for record in obj:
                            record['id'] = email_obj['id']
                            record['from'] = email_obj['from']
                            record['date'] = email_obj['date']
                            with open(output_json, 'a') as f:
                                json.dump(record, f, indent=4)
                    else:
                        logging.error("Processing failed after 3 retries")
                        error_data = {
                            'part': part,
                            'from': email_obj['from'],
                            'date': email_obj['date']
                        }
                        with open(error_file, 'a') as f:
                            json.dump(error_data, f, indent=4)

if __name__ == '__main__':
    os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
    user_email = 'jordanbaird0@gmail.com'
    newsletter_processor = TLDRNewsletterProcessor(user_email)
    emails = newsletter_processor.fetch_emails()
    newsletter_processor.process_emails(emails)
