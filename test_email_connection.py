#!/usr/bin/env python3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Test SMTP connection
def test_smtp_connection():
    print("Testing SMTP connection...")
    
    # Your Railway environment variables
    email_host = 'smtpout.secureserver.net'
    email_port = 587
    email_user = 'finance@braysint.com'
    email_password = 'Ihji272@j_6Qp3#NnTb29@_2'
    
    try:
        # Connect to server
        server = smtplib.SMTP(email_host, email_port)
        server.set_debuglevel(1)  # Enable debug output
        server.starttls()  # Enable TLS
        
        print(f"Attempting to login with user: {email_user}")
        server.login(email_user, email_password)
        
        print("✅ SMTP connection successful!")
        server.quit()
        return True
        
    except Exception as e:
        print(f"❌ SMTP connection failed: {e}")
        return False

if __name__ == "__main__":
    test_smtp_connection()
