import requests
from datetime import datetime

API_URL = "http://localhost:8000/api"

def calculate_sla(ticket_id):
    """
    Calcula el estado del SLA (Service Level Agreement) de un ticket.

    Debe obtener el ticket de la API, mirar su fecha de creación (created_at)
    y compararla con la fecha actual.

    Criterios de ejemplo:
    - Prioridad 'high': SLA violado si > 4 horas.
    - Prioridad 'medium': SLA violado si > 24 horas.
    - Prioridad 'low': SLA violado si > 48 horas.

    Args:
        ticket_id (int): ID del ticket.

    Returns:
        str: Estado del SLA ('On Time', 'Warning', 'Viablated').
    """
    # Estudiante: Implementar cálculo de SLA
    pass
    raise NotImplementedError("Estudiante: Implementar lógica de SLA")
