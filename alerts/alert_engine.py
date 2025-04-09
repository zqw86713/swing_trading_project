import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_alert(symbol: str, message: str,
                email_to: str = "your_email@example.com",
                email_from: str = "your_email@example.com",
                smtp_server: str = "smtp.gmail.com",
                smtp_port: int = 587,
                username: str = "your_email@example.com",
                password: str = "your_app_password"):
    subject = f"Trading Alert: {symbol}"
    body = f"Symbol: {symbol}\nAlert: {message}"

    msg = MIMEMultipart()
    msg["From"] = email_from
    msg["To"] = email_to
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(username, password)
            server.sendmail(email_from, email_to, msg.as_string())
            print(f"Alert sent: {subject}")
    except Exception as e:
        print(f"Failed to send alert: {e}")
