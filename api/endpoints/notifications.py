from fastapi import APIRouter
from models.notification import NotificationRequest

router = APIRouter()

@router.post("/notifications")
async def send_notification(notification: NotificationRequest):
    return {"message": "Notification sent successfully"}