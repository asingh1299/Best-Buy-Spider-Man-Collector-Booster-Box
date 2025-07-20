import os

from spidey.best_buy import check_if_best_buy_item_sellable
from spidey.email import email_user


def main():
    SKU_ID = os.environ.get("SPIDERMAN_SKU", "6621977")

    # Email config
    sender_email = os.environ["EMAIL_USER"]
    receiver_emails = os.environ["EMAIL_RECIPIENTS"].split(",")
    receiver_emails = [email.strip() for email in receiver_emails]
    subject = "Test: SPIDERMAN AVAILABLE!"
    body = f"Test: Spiderman (SKU {SKU_ID}) is now available at Best Buy!"

    smtp_server = os.environ.get("SMTP_SERVER", "smtp.gmail.com")
    smtp_port = int(os.environ.get("SMTP_PORT", "587"))
    # Go to Google Accounts -> App passwords -> Create an app password for this script
    smtp_password = os.environ["EMAIL_PASS"]

    print("Starting availability check...")

    available = check_if_best_buy_item_sellable(skuId=SKU_ID)

    if not available:
        print("SPIDERMAN IS AVAILABLE! Sending email...")
        try:
            for receiver_email in receiver_emails:
                email_user(
                    sender_email=sender_email,
                    receiver_email=receiver_email,
                    subject=subject,
                    body=body,
                    smtp_server=smtp_server,
                    smtp_port=smtp_port,
                    smtp_password=smtp_password,
                )
            print("Email(s) sent. Exiting loop.")
        except Exception as e:
            print(f"Error sending email: {e}")
    else:
        print("Still unavailable.")


if __name__ == "__main__":
    main()
