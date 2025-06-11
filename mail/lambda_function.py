import json
import boto3
import logging
from string import Template

def lambda_handler(event, context):
    """
    Lambda entry point for sending emails to a list of customers using Amazon SES.
    Expects event to contain necessary data (e.g., email subject, body, etc.).
    """
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Example: Log the incoming event
    logger.info(f"Received event: {json.dumps(event)}")

    emails = get_email_addresses()
    template = get_email_template()
    subject = "Your Subject Here"  # TODO: Extract subject from event or define it

    # Send emails
    results = send_emails_ses(emails, template, subject)

    # TODO: Handle results, e.g., log them, return in response, etc.

    return {
        'statusCode': 200,
        'body': json.dumps('Lambda executed successfully!')
    }

def get_email_addresses():
    """
    Returns a list of email addresses. Stub for Google Sheets integration.
    TODO: Replace with actual Google Sheets fetch logic.
    """
    return [
        f"user{i}@example.com" for i in range(1, 11)
    ]

def get_email_template():
    """
    Reads the email template from emailbody.markdown and returns it as a string.
    """
    with open("emailbody.markdown", "r") as f:
        return f.read()

def send_emails_ses(emails, template_str, subject):
    """
    Sends emails using Amazon SES. Pure function, returns list of (email, status) tuples.
    """
    ses = boto3.client('ses')
    results = []
    for email in emails:
        body = Template(template_str).substitute(email=email)
        try:
            response = ses.send_email(
                Source='no-reply@example.com',
                Destination={'ToAddresses': [email]},
                Message={
                    'Subject': {'Data': subject},
                    'Body': {'Html': {'Data': body}}
                }
            )
            results.append((email, 'sent'))
        except Exception as e:
            results.append((email, f'error: {str(e)}'))
    return results
