from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from enum import Enum

class RoleEnum(str, Enum):
    admin = "admin"
    tecnico = "tecnico"
    cliente = "cliente"

class PriorityEnum(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class StatusEnum(str, Enum):
    open = "open"
    in_progress = "in_progress"
    closed = "closed"

class UserBase(BaseModel):
    username: str
    role: RoleEnum

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    class Config:
        orm_mode = True

class TicketBase(BaseModel):
    title: str
    description: str
    priority: PriorityEnum

class TicketCreate(TicketBase):
    pass

class TicketUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[PriorityEnum] = None
    status: Optional[StatusEnum] = None
    technician_id: Optional[int] = None
    resolution_notes: Optional[str] = None # Added for resolution context

class Ticket(TicketBase):
    id: int
    status: StatusEnum
    created_at: datetime
    resolved_at: Optional[datetime] = None
    technician_id: Optional[int] = None
    
    class Config:
        orm_mode = True
