from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, database
import datetime

router = APIRouter(prefix="/api", tags=["persistence"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Users
@router.get("/users", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(models.User).filter(models.User.role == "tecnico").offset(skip).limit(limit).all()
    return users

@router.post("/login")
def login(credentials: dict, db: Session = Depends(get_db)):
    # Simple login logic for persistence layer
    user = db.query(models.User).filter(models.User.username == credentials.get("username")).first()
    if not user or user.password != credentials.get("password"):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"token": "fake-jwt-token", "user": {"id": user.id, "username": user.username, "role": user.role}}

# Tickets
@router.post("/tickets", response_model=schemas.Ticket)
def create_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db)):
    db_ticket = models.Ticket(**ticket.dict())
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket

@router.get("/tickets", response_model=List[schemas.Ticket])
def read_tickets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tickets = db.query(models.Ticket).offset(skip).limit(limit).all()
    return tickets

@router.get("/tickets/{ticket_id}", response_model=schemas.Ticket)
def read_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = db.query(models.Ticket).filter(models.Ticket.id == ticket_id).first()
    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket

@router.put("/tickets/{ticket_id}", response_model=schemas.Ticket)
def update_ticket(ticket_id: int, ticket_update: schemas.TicketUpdate, db: Session = Depends(get_db)):
    db_ticket = db.query(models.Ticket).filter(models.Ticket.id == ticket_id).first()
    if db_ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    
    update_data = ticket_update.dict(exclude_unset=True)
    if "status" in update_data and update_data["status"] == "closed":
        db_ticket.resolved_at = datetime.datetime.utcnow()
    
    # Remove resolution_notes from update_data before mapping to model if it's not in model
    # Note: Model doesn't have resolution_notes in spec, but logic layer might need to log it or store it.
    # For now, we update what matches columns.
    
    for key, value in update_data.items():
        if hasattr(db_ticket, key) and key != "resolution_notes":
            setattr(db_ticket, key, value)
            
    db.commit()
    db.refresh(db_ticket)
    return db_ticket
