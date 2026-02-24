""""
Archivo para el manejo de ficheros Json
"""

# Biblioteca para el manejo de ficheros json
import json


def guardar_tareas(tareas: list, ruta: str):
    """
    Función para guardar los datos de las tareas en un archivo json

    Args:
        tareas (list): Lista donde se almacenan las tareas (diccionarios)
        ruta (str): Ruta donde se almacena el json
    """
    with open(ruta, 'w', encoding='utf-8') as f:
        json.dump(tareas, f, indent=4)


def cargar_tareas(
        ruta: str, msg_fichero_cargado: str, msg_nuevo_fichero: str, msg_corrupto: str
) -> list:
    """
    Función para leer y cargar el arcivo json de tareas

    Args:
        ruta (str): Ruta donde se almacena el archivo
        msg_fichero_cargado: Mensaje de fichero cargado
        msg_nuevo_fichero: Mensaje de nuevo fichero
        msg_corrupto(str): Mensaje de fichero corrupto, se crea uno nuevo.

    Returns:
        list: Lista de tareas
    """
    # Control del error del archivo no existe o corrupto
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            datos_tareas = json.load(f)
            print(msg_fichero_cargado)
            return datos_tareas
    except FileNotFoundError:
        datos_tareas = []
        print(msg_nuevo_fichero)
        return datos_tareas
    except json.JSONDecodeError:
        datos_tareas = []
        print(msg_corrupto)
        return datos_tareas
