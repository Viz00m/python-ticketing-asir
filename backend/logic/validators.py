
def validate_api_response(response):
    """
    Valida si una respuesta de la API es correcta (status 200-299).

    Si la respuesta trae un error (4xx, 5xx), debe lanzar una excepción o retorna False.

    Args:
        response (requests.Response): Objeto respuesta de la librería requests.

    Returns:
        bool: True si es válida.
        Raises: Exception con el mensaje de error si no es válida.
    """
    # Estudiante: Implementar validación de respuesta
    pass
    raise NotImplementedError("Estudiante: Implementar validación de respuesta API")
