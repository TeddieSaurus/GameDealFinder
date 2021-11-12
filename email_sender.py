import smtplib
import config

# Constants


class EmailSender():
    def __init__(self):
        pass

    def send_email(self, text_to_email):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=config.MY_EMAIL, password=config.MY_PASSWORD)
            connection.sendmail(
                from_addr=config.MY_EMAIL,
                to_addrs=config.RECEIVING_EMAIL,
                msg=f"Subject:Game on your List is on Sale!\n\n{text_to_email}"
            )