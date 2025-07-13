#!/usr/bin/env python3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Test different SMTP configurations
def test_smtp_configurations():
    email_user = 'finance@braysint.com'
    email_password = 'Ihji272@j_6Qp3#NnTb29@_2'
    
    configurations = [
        # GoDaddy SMTP (current)
        {'host': 'smtpout.secureserver.net', 'port': 587, 'tls': True, 'ssl': False},
        # GoDaddy SMTP SSL
        {'host': 'smtpout.secureserver.net', 'port': 465, 'tls': False, 'ssl': True},
        # Alternative GoDaddy SMTP
        {'host': 'relay-hosting.secureserver.net', 'port': 25, 'tls': True, 'ssl': False},
        # GoDaddy Workspace SMTP
        {'host': 'smtp.office365.com', 'port': 587, 'tls': True, 'ssl': False},
    ]
    
    for i, config in enumerate(configurations):
        print(f"\n--- Testing configuration {i+1} ---")
        print(f"Host: {config['host']}, Port: {config['port']}, TLS: {config['tls']}, SSL: {config['ssl']}")
        
        try:
            if config['ssl']:
                server = smtplib.SMTP_SSL(config['host'], config['port'])
            else:
                server = smtplib.SMTP(config['host'], config['port'])
            
            server.set_debuglevel(0)  # Disable debug for cleaner output
            
            if config['tls'] and not config['ssl']:
                server.starttls()
            
            server.login(email_user, email_password)
            print(f"✅ Configuration {i+1} successful!")
            server.quit()
            return config
            
        except Exception as e:
            print(f"❌ Configuration {i+1} failed: {e}")
    
    return None

if __name__ == "__main__":
    successful_config = test_smtp_configurations()
    if successful_config:
        print(f"\n🎉 Working configuration found: {successful_config}")
    else:
        print("\n❌ No working configuration found. Check your email credentials and account settings.")
