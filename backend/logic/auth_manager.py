import requests

API_URL = "http://localhost:8000/api"

token = None
usuario_actual = None

def login(username, password):
   
    global token, usuario_actual

    respuesta = requests.post(
        f"{API_URL}/login",
        json={"username": username, "password": password}
    )

    if respuesta.status_code == 200:
        datos = respuesta.json()
        token = datos["token"]
        usuario_actual = datos["user"]
        return datos
    else:
        return None

def check_permission(role):
   
    if usuario_actual is None:
        return False

    jerarquia = {"admin": 3, "tecnico": 2, "cliente": 1}
    nivel_usuario   = jerarquia.get(usuario_actual["role"], 0)
    nivel_requerido = jerarquia.get(role, 99)

    return nivel_usuario >= nivel_requerido
