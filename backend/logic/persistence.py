import csv
import os
from datetime import datetime

def export_to_csv(data, filename="export.csv"):
    """
    Exporta una lista de diccionarios a un archivo CSV.

    Args:
        data (list[dict]): Datos a exportar.
        filename (str): Nombre del archivo de destino.

    Returns:
        str: Ruta absoluta del archivo creado.
    """
    # Estudiante: Implementar exportación a CSV
    pass
    raise NotImplementedError("Estudiante: Implementar exportación a CSV")

def system_logger(message, level="INFO"):
    """
    Registra un mensaje en un archivo de log del sistema (system.log).

    Formato sugerido: [FECHA_HORA] [LEVEL] Mensaje

    Args:
        message (str): Mensaje a loguear.
        level (str): Nivel de log (INFO, ERROR, WARN).
    """
    # Estudiante: Implementar writing a archivo de texto
    pass
    raise NotImplementedError("Estudiante: Implementar logger")
