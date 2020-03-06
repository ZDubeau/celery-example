from datetime import datetime
from time import sleep


emails = []


def talking_clock() -> datetime:
    clk = datetime.now()
    print(f"Current time: {clk}")
    return datetime.now()


def subscribe_to_newsletter(email: str) -> None:
    print(f"Adding {email} to newsletter subscribers")
    print("Checking some stuff, be patient...")
    sleep(5)
    emails.append(email)


def send_newsletter() -> None:
    print("Sending newsletter to all subscribers:")
    print(emails)
