import smtplib
from email.mime.text import MIMEText

def send_alert(filename, action):
    sender_email = "your_email@gmail.com"
    receiver_email = "receiver_email@gmail.com"
    subject = "File Integrity Alert"
    body = f"Alert! File {filename} was {action}."

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login("your_email@gmail.com", "your_password")
        server.sendmail(sender_email, receiver_email, msg.as_string())

    print("Alert sent!")
