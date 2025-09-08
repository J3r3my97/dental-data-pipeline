from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List

# User schemas
class UserBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    phone: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

# Authentication schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Patient Profile schemas
class PatientProfileCreate(BaseModel):
    last_dental_visit: Optional[str] = None
    dental_concerns: Optional[str] = None
    current_medications: Optional[str] = None
    allergies: Optional[str] = None
    dental_history: Optional[str] = None
    pain_level: Optional[int] = None
    insurance_provider: Optional[str] = None
    emergency_contact_name: Optional[str] = None
    emergency_contact_phone: Optional[str] = None

class PatientProfileResponse(PatientProfileCreate):
    id: int
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

# Appointment schemas
class AppointmentCreate(BaseModel):
    appointment_date: datetime
    appointment_type: str
    notes: Optional[str] = None

class AppointmentResponse(AppointmentCreate):
    id: int
    user_id: int
    status: str
    created_at: datetime
    
    class Config:
        from_attributes = True

# Radiograph schemas
class RadiographResponse(BaseModel):
    id: int
    filename: str
    original_filename: str
    file_size: int
    upload_date: datetime
    description: Optional[str] = None
    
    class Config:
        from_attributes = True