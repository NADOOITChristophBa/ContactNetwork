from O365 import Account
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the credentials from the environment variables
credentials = (os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))

account = Account(credentials)
if account.authenticate(scopes=["basic", "calendar_all"]):
    print("Authenticated!")

mailbox = account.mailbox()
inbox = mailbox.inbox_folder()

for message in inbox.get_messages():
    print(message)
