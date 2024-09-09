import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
def send_mail(sender_mail, sender_p, receiver_det, email_body, mail_title):
    sender_email = sender_mail
    receiver_email = receiver_det['email1']
    subject = mail_title
    message = email_body

    # Gmail SMTP server configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = sender_mail
    smtp_password = sender_p

    # Create the email message
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "html"))
    
    # Connect to Gmail's SMTP server
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        
        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())
        
        print("Email sent successfully!")
        
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the server connection
        server.quit()