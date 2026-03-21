import smtplib
from email.mime.text import MIMEText
from email.header import Header
from config import EMAIL, PASSWORD, RECEIVER

def send_email(report):
    msg = MIMEText(report, "plain", "utf-8")  # ✅ חשוב!

    msg["Subject"] = Header("סיכום מכירות", "utf-8")  # ✅ חשוב!
    msg["From"] = EMAIL
    msg["To"] = RECEIVER

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)

    print("Email sent successfully!")