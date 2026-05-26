import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from .database import Base
import enum

class Role(str, enum.Enum):
    admin = "admin"
    tecnico = "tecnico"
    cliente = "cliente"

class Priority(str, enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"

class Status(str, enum.Enum):
    open = "open"
    in_progress = "in_progress"
    closed = "closed"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)  # In validation we should hash this, but for simplicity we store as is or hashed
    role = Column(String) # Stored as string to match requirements easier, but could be Enum

    # Relationships can be added if needed, e.g. tickets assigned
    tickets_assigned = relationship("Ticket", back_populates="technician")

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    priority = Column(String, default="medium") # low, medium, high
    status = Column(String, default="open") # open, in_progress, closed
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    resolved_at = Column(DateTime, nullable=True)
    technician_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    
    technician = relationship("User", back_populates="tickets_assigned")
    # creator_id could be added if we tracked who created it
