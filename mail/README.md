# AWS Lambda Email Service with Amazon SES and Google Sheets

## Architecture Diagram

```mermaid
sequenceDiagram
    participant Client as HTTP Client
    participant Lambda as Lambda Function (Python)
    participant Sheets as Google Sheets
    participant Source as Email Source
    participant SES as Amazon SES
    participant Logs as CloudWatch Logs
    participant Inbox as Customer Inbox

    Client->>Lambda: HTTP Request (Trigger Event)
    Lambda->>Sheets: Fetch Customer List
    Sheets-->>Lambda: Customer List
    Lambda->>Source: Get Email Template/Body
    Source-->>Lambda: Email Content
    Lambda->>SES: Send Email(s)
    SES-->>Inbox: Deliver Email(s)
    Lambda->>Logs: Log/Status
    Lambda-->>Client: HTTP Response (Result)
```

## Description
- The Lambda function (Python) is triggered by an HTTP request containing the event data.
- It fetches the customer list from Google Sheets.
- It uses an email source (template/body) for the message content.
- For each customer, it sends an email using Amazon SES.
- Logs and status are sent to CloudWatch.
- Emails are delivered to customer inboxes.

## Next Steps
- Set up AWS Lambda and SES permissions.
- Configure access to Google Sheets API.
- Implement the Lambda function in Python.
