"""
Lógica del proyecto:
El sistema debe permitir administrar una lista de tareas pendientes,
proporcionando las funciones necesarias para crear, listar, completar
y eliminar elementos de la colección.
"""


def agregar_tarea(lista_tareas: list, descripcion: str, prioridad: str):
    """
    Función para agregar tareas a la lista de tareas, las tareas se almacenan
    en un diccionario con la siguiente estructura:
    - id(int): Identificado único.
    - descripción(str): Descripción de la tarea.
    - prioridad(str): Alta, Media o Baja.
    - completado(bool): Estado de la tarea (inicia en False).

    Args:
        lista_tareas (list): Lista donde se almacenan las tareas.
        description (str): Descripción de la tarea.
        prioridad (str): Prioridad de la tarea.
    """
    # Si no hay elementos en la lista
    if not lista_tareas:
        # Establecemos el primer id
        id_task = 1
    # De lo contrario
    else:
        # Debemos busca el ID más alto y sumar uno
        id_task = max(tarea['id'] for tarea in lista_tareas) + 1
    # Generamos diccionario con la tarea almacenada
    tarea = {
        "id": id_task,
        "descripcion": descripcion,
        "prioridad": prioridad,
        "completada": False
    }
    # añadimos tarea a la lista de tareas:
    lista_tareas.append(tarea)


def obtener_tareas(lista_tareas: list) -> list:
    """
    Función para devolver la lista de la tareas

    Args:
        lista_tareas (list): Lista de tareas

    Returns:
        list: Lista de tareas
    """
    # Devolvemos una copia de la lista de tareas
    return lista_tareas.copy()


def completar_tarea(lista_tareas: list, id_tarea: int) -> bool:
    """
    Función para completar tareas dentro de la lista de tareas.

    Args:
        lista_tareas (list): Lista de tareas.
        id_tarea (int): ID de la tarea a completar.

    Returns:
        bool: Resultado de completar la tarea
    """
    # Recorremos la lista de tareas
    for tarea in lista_tareas:
        # Si la tarea existe modificamos compeletada a True y devolvmeos True
        if tarea["id"] == id_tarea:
            tarea["completada"] = True
            return True
    # Si sale de bucle sin encontrar la tarea es que no se exite.
    return False


def eliminar_tareas(lista_tareas: list, id_tarea: int) -> bool:
    """
    Función para elminar tareas de la lista

    Args:
        lista_tareas (list): Lista de tareas
        id_tarea (int): ID de la tarea a eliminar

    Returns:
        bool: Resultado de eliminar la tarea
    """
    # Comprobamos que el Id se encuntra en la lista de tareas
    for tarea in lista_tareas:
        # Si la tarea existe la eliminamos de la lista y devolvemos True
        if tarea["id"] == id_tarea:
            lista_tareas.remove(tarea)
            return True
    # Si sale del bucle sin encontrar la tarea es que no existe
