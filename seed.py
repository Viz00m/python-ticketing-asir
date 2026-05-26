import requests
from backend.database import SessionLocal, engine
from backend.models import Base, User, Ticket
from backend import models
from passlib.context import CryptContext

# Initial setup
Base.metadata.create_all(bind=engine)
db = SessionLocal()

def seed_data():
    print("Seeding data...")
    
    # Check if admin exists
    if db.query(User).filter(User.username == "admin").first():
        print("Data already exists. Skipping.")
        return

    # Create Users
    users = [
        User(username="admin", password="password", role="admin"),
        User(username="tech1", password="password", role="tecnico"),
        User(username="tech2", password="password", role="tecnico"),
        User(username="client1", password="password", role="cliente"),
    ]
    
    db.add_all(users)
    db.commit()
    
    # Get tech IDs
    tech1 = db.query(User).filter(User.username == "tech1").first()
    
    # Create Tickets
    tickets = [
        Ticket(title="Printer not working", description="Hp Laserjet 1020 is jammed", priority="high", status="open", technician_id=tech1.id),
        Ticket(title="VPN Access", description="Requesting VPN access for remote work", priority="medium", status="in_progress", technician_id=None),
        Ticket(title="Screen flickering", description="Monitor turns off randomly", priority="low", status="open", technician_id=None),
        Ticket(title="Password Reset", description="User forgot password", priority="high", status="closed", technician_id=tech1.id),
    ]
    
    db.add_all(tickets)
    db.commit()
    print("Seeding complete!")

if __name__ == "__main__":
    seed_data()
    db.close()
