import logging
import imaplib
import email

# Configure logger
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

def fetch_and_classify_emails(email_address, password):
    try:
        # Connect to the email server
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(email_address, password)
        mail.select("inbox")

        # Fetch emails
        _, data = mail.search(None, "ALL")
        email_ids = data[0].split()
        emails = []
        for email_id in email_ids[:5]:  # Fetch the latest 5 emails
            _, msg_data = mail.fetch(email_id, "(RFC822)")
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    emails.append(msg.get("Subject"))

        # Classify emails (dummy classification for now)
        classified_emails = [{"subject": subject, "category": "General"} for subject in emails]
        return classified_emails
    except Exception as e:
        logger.error(f"Error fetching emails: {e}")
        return [{"subject": "Error", "category": "Failed to fetch emails"}]