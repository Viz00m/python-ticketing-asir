import requests
from backend.logic.auth_manager import API_URL, token

def create_ticket(ticket_data):
  
    respuesta = requests.post(
        f"{API_URL}/tickets",
        json={
            "title":       ticket_data["title"],
            "description": ticket_data["description"],
            "priority":    ticket_data["priority"]
        },
        headers={"Authorization": f"Bearer {token}"}
    )

    if respuesta.status_code == 200:
        return respuesta.json()  
    else:
        raise Exception(f"Error al crear ticket: {respuesta.status_code}")

def resolve_ticket(ticket_id, resolution_notes):
    
    respuesta = requests.put(
        f"{API_URL}/tickets/{ticket_id}",
        json={
            "status":           "closed",
            "resolution_notes": resolution_notes
        },
        headers={"Authorization": f"Bearer {token}"}
    )

    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        raise Exception(f"Error al resolver ticket: {respuesta.status_code}")

def reopen_ticket(ticket_id):
    
    respuesta = requests.put(
        f"{API_URL}/tickets/{ticket_id}",
        json={"status": "open"},
        headers={"Authorization": f"Bearer {token}"}
    )

    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        raise Exception(f"Error al reabrir ticket: {respuesta.status_code}")
