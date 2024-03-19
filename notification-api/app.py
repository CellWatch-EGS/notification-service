from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class NotificationRequest(BaseModel):
    username: str
    email: str
    phoneNumber: str
    systemName: str
    notificationContent: dict
    preferences: dict

@app.post("/v1/notifications")
async def send_notification(notification: NotificationRequest):
    
    return {"message": "Notification sent successfully"}