from fastapi import FastAPI
from .database import engine, Base
from .routes import persistence

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Python-Ticketing ASIR Suite")

# Include routers
app.include_router(persistence.router)

@app.get("/")
def root():
    return {"message": "System Operational"}
