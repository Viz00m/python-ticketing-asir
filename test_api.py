import requests
import time

URL_BASE = "https://api-asir.vlabnode.com"
ALUMNO_STR = "caye_159"

CREDENTIALS = {
    "admin": {"username": "admin", "password": "adm123"},
}

def test_flow():
    print(f"🚀 Iniciando test para {ALUMNO_STR}...\n")

    login_headers = {"X-Alumno-Username": ALUMNO_STR}

    try:
        # 1. LOGIN
        print("0. Haciendo login...")
        res = requests.post(f"{URL_BASE}/login", json=CREDENTIALS["admin"], headers=login_headers)
        if res.status_code != 200:
            print(f"❌ Error en Login: {res.status_code} - {res.text}")
            return

        data_admin = res.json()
        token = data_admin["token"]
        user_id = data_admin["user_id"]
        print(f"✅ Login OK — user_id: {user_id}, token: {token[:20]}...")

        headers = {
    "Authorization": f"Bearer {token}",
    "X-Alumno-Username": ALUMNO_STR,
    "X-User-Id": str(user_id)
}

        # 2. CREAR UN TICKET
        print("\n1. Creando ticket de prueba...")
        ticket_data = {
            "titulo": "Ticket de prueba - Victoriano",
            "descripcion": "Probando conexión real con la API del profesor",
            "criticidad_id": 2,
            "user_id_creador": user_id
        }
        res_ticket = requests.post(f"{URL_BASE}/tickets", json=ticket_data, headers=headers)
        if res_ticket.status_code not in (200, 201):
            print(f"❌ Error creando ticket: {res_ticket.status_code} - {res_ticket.text}")
            return
        ticket_id = res_ticket.json()["ticket_id"]
        print(f"✅ Ticket creado con ID: {ticket_id}")

        # 3. AÑADIR COMENTARIO Y CAMBIO DE ESTADO
        print(f"\n2. Actualizando ticket {ticket_id}...")
        update_data = {
            "user_id_editor": user_id,
            "estado_id": 2,
            "comentario": "Ticket en progreso - test automático vict_482"
        }
        res_update = requests.put(f"{URL_BASE}/tickets/{ticket_id}", json=update_data, headers=headers)
        print(f"✅ Actualización: {res_update.status_code}")

        # 4. RECUPERAR DETALLES
        print(f"\n3. Recuperando detalle del ticket {ticket_id}...")
        res_detail = requests.get(f"{URL_BASE}/tickets/{ticket_id}", headers=headers)
        if res_detail.status_code == 200:
            detalle = res_detail.json()
            print(f"✅ Título: {detalle.get('titulo')}")
            print(f"   Estado: {detalle.get('current_status')}")
            print(f"   Historial: {detalle.get('historial', [])}")
            print(f"   Comentarios: {detalle.get('comentarios', [])}")
        else:
            print(f"❌ Error recuperando detalle: {res_detail.status_code}")

        # 5. LISTAR TODOS TUS TICKETS
        print(f"\n4. Listando todos los tickets de {ALUMNO_STR}...")
        res_list = requests.get(f"{URL_BASE}/tickets", headers=headers)
        if res_list.status_code == 200:
            lista = res_list.json()
            print(f"✅ Total de tickets: {len(lista)}")
        else:
            print(f"❌ Error listando: {res_list.status_code}")

        # 6. LOGOUT
        print("\n5. Cerrando sesión...")
        requests.post(f"{URL_BASE}/logout", headers=headers)
        print("✅ Logout OK")

        print("\n🎉 TEST COMPLETO CON LA API DEL PROFESOR")

    except Exception as e:
        print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    test_flow()