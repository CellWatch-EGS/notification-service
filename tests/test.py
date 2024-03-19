import requests

api_url = "http://localhost:8080/v1/notifications"

notification_data = {
    "username": "john_doe",
    "email": "john@example.com",
    "phoneNumber": "+1234567890",
    "systemName": "MySystem",
    "notificationContent": {
        "subject": "Test Notification",
        "body": "This is a test notification."
    },
    "preferences": {
        "smsEnabled": True,
        "emailEnabled": True,
        "pushEnabled": False
    }
}

response = requests.post(api_url, json=notification_data)

print(response.status_code, " ", response.json())