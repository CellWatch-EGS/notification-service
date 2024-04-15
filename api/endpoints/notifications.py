from fastapi import APIRouter, HTTPException
from models.notification import NotificationRequest
from utils.notification_utils import send_sms, send_email

router = APIRouter()

@router.post("/notifications")
async def send_notification(notification: NotificationRequest):
    try:
        if notification.preferences["smsEnabled"]:
            send_sms(notification.phoneNumber, notification.notificationContent["body"])
        
        if notification.preferences["emailEnabled"]:
            send_email(notification.email, notification.notificationContent["subject"], notification.notificationContent["body"])

        if notification.preferences["pushEnabled"]:
            pass
        
        return {"message": "Notification(s) sent successfully"}
    except Exception as e:
        print(f"An error occurred while sending notifications: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while sending notifications")