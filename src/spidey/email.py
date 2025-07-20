import smtplib
from email.message import EmailMessage


def email_user(
    sender_email: str,
    receiver_email: str,
    subject: str,
    body: str,
    smtp_server: str,
    smtp_port: str,
    smtp_password: str,
):
    """
    Helper to send email notifications.
    """
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, smtp_password)
            server.send_message(msg)
    except Exception as e:
        print(f"Failed to send email: {e}")
