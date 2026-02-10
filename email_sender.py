import smtplib
from email.mime.text import MIMEText
from secrets import sender, receiver, password


msg = MIMEText("Hello! This email was sent using Python.")
msg["Subject"] = "Python Email Test"
msg["From"] = sender
msg["To"] = receiver

# Connect to Gmail SMTP
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()           # Secure connection
    server.login(sender, password)
    server.send_message(msg)

print("Email sent successfully!")
