from pydantic import BaseModel, EmailStr
from typing_extensions import TypedDict

class NotificationContent(TypedDict):
    subject: str
    body: str

class Preferences(TypedDict):
    smsEnabled: bool
    emailEnabled: bool
    pushEnabled: bool

class NotificationRequest(BaseModel):
    username: str
    email: EmailStr
    phoneNumber: str
    systemName: str
    notificationContent: NotificationContent
    preferences: Preferences