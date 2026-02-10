import smtplib
from email.message import EmailMessage
from secrets import sender, receiver, password

def send_email(receiver_email: str, subject: str, content: str):
    """Send an email to the specified receiver with the given subject and content."""

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = receiver_email
    msg.set_content(content)

    # Connect to Gmail SMTP
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()           # Secure connection
        server.login(sender, password)
        server.send_message(msg)

    print("Email sent successfully!")
if __name__ == "__main__":
    send_email(receiver_email="4mh23cs083@gmail.com",subject="Python Email Test",content="Hello! This email was sent using Python.")
