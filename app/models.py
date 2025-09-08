from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    is_active = Column(Boolean, default=True)
    
    # Relationships
    patient_profile = relationship("PatientProfile", back_populates="user", uselist=False)
    appointments = relationship("Appointment", back_populates="user")
    radiographs = relationship("Radiograph", back_populates="user")

class PatientProfile(Base):
    __tablename__ = "patient_profiles"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    
    # Dental questionnaire fields
    last_dental_visit = Column(String)
    dental_concerns = Column(Text)
    current_medications = Column(Text)
    allergies = Column(Text)
    dental_history = Column(Text)
    pain_level = Column(Integer)  # 1-10 scale
    insurance_provider = Column(String)
    emergency_contact_name = Column(String)
    emergency_contact_phone = Column(String)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    user = relationship("User", back_populates="patient_profile")

class Appointment(Base):
    __tablename__ = "appointments"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    appointment_date = Column(DateTime, nullable=False)
    appointment_type = Column(String, nullable=False)  # cleaning, consultation, etc.
    status = Column(String, default="scheduled")  # scheduled, completed, cancelled
    notes = Column(Text, nullable=True)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    user = relationship("User", back_populates="appointments")

class Radiograph(Base):
    __tablename__ = "radiographs"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    filename = Column(String, nullable=False)
    original_filename = Column(String, nullable=False)
    file_path = Column(String, nullable=False)
    file_size = Column(Integer)
    upload_date = Column(DateTime(timezone=True), server_default=func.now())
    description = Column(Text, nullable=True)
    
    # Relationships
    user = relationship("User", back_populates="radiographs")