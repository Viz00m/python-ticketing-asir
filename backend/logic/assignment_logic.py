import requests
from backend.logic.auth_manager import API_URL, token

def smart_assign(ticket_id):
    
    cabeceras = {"Authorization": f"Bearer {token}"}

    tecnicos = requests.get(f"{API_URL}/users", headers=cabeceras).json()

    tickets = requests.get(f"{API_URL}/tickets", headers=cabeceras).json()

    carga = {}
    for tecnico in tecnicos:
        carga[tecnico["id"]] = 0  # empezamos todos a 0

    for ticket in tickets:
        tid = ticket.get("technician_id")
        if tid in carga and ticket["status"] != "closed":
            carga[tid] += 1

    tecnico_elegido = min(carga, key=lambda id: carga[id])

    respuesta = requests.put(
        f"{API_URL}/tickets/{ticket_id}",
        json={"technician_id": tecnico_elegido},
        headers=cabeceras
    )

    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        raise Exception(f"Error al asignar: {respuesta.status_code}")
