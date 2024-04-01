from pydantic import BaseModel, EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber
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
    phoneNumber: PhoneNumber
    systemName: str
    notificationContent: NotificationContent
    preferences: Preferences