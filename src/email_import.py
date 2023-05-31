from O365 import Account, FileSystemTokenBackend
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the credentials from the environment variables
credentials = (os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))

# Specify token path (using FileSystemTokenBackend for simplicity here)
token_backend = FileSystemTokenBackend(token_path=".", token_filename="o365_token.txt")

# Instantiate the Account object
account = Account(credentials, token_backend=token_backend)

# Check if we are authenticated
if not account.is_authenticated:
    # Authenticate here
    account.authenticate(scopes=["basic", "calendar_all"])

# Instantiate the mailbox object
mailbox = account.mailbox()

# Access the Inbox
inbox = mailbox.inbox_folder()


def import_emails():
    # Get messages from the Inbox
    for message in inbox.get_messages():
        print(message)


# Call the function
import_emails()
