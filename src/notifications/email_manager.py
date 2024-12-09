from typing import Dict
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailManager:
    def __init__(self, smtp_config: Dict):
        self.smtp_config = smtp_config
    
    def send_billing_notification(self, user_email: str, event_type: str, details: Dict):
        """Send billing-related notifications"""
        templates = {
            'payment_success': {
                'subject': 'Payment Successful - Marketing Automation Suite',
                'body': f"Your payment of ${details['amount']} was successful. Next billing date: {details['next_date']}"
            },
            'payment_failed': {
                'subject': 'Payment Failed - Action Required',
                'body': f"Your payment of ${details['amount']} failed. Please update your payment method."
            },
            'subscription_renewal': {
                'subject': 'Subscription Renewal Reminder',
                'body': f"Your subscription will renew on {details['renewal_date']}. Amount: ${details['amount']}"
            }
        }
        
        template = templates.get(event_type)
        if template:
            self._send_email(user_email, template['subject'], template['body'])
    
    def send_usage_report(self, user_email: str, usage_data: Dict):
        """Send monthly usage reports"""
        subject = f"Your Monthly Usage Report - {datetime.now().strftime('%B %Y')}"
        body = self._format_usage_report(usage_data)
        self._send_email(user_email, subject, body)
    
    def _format_usage_report(self, usage_data: Dict) -> str:
        return f"""
        Monthly Usage Summary:
        - Posts Published: {usage_data['posts_published']}
        - Engagement Rate: {usage_data['engagement_rate']}%
        - Top Performing Post: {usage_data['top_post']}
        - API Calls: {usage_data['api_calls']}
        - Storage Used: {usage_data['storage_used']}MB
        """
    
    def _send_email(self, to_email: str, subject: str, body: str):
        msg = MIMEMultipart()
        msg['From'] = self.smtp_config['from_email']
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        with smtplib.SMTP(self.smtp_config['host'], self.smtp_config['port']) as server:
            server.starttls()
            server.login(self.smtp_config['username'], self.smtp_config['password'])
            server.send_message(msg)