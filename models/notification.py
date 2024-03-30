from pydantic import BaseModel

class NotificationRequest(BaseModel):
    username: str
    email: str
    phoneNumber: str
    systemName: str
    notificationContent: dict
    preferences: dict