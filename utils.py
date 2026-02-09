"""
Lógica de apoyo a main
"""


def mostrar_menu():
    """
    Función para mostrar menú
    """
    while True:
        # Menu de acciones de la app
        print("+-----------------------------------+")
        print("|  ✍ Gestor de tareas 1.0           |")
        print("+-----------------------------------+")
        print("| 1 - Agregar tarea.                |")
        print("| 2 - Completar tarea.              |")
        print("| 3 - Elminar tarea.                |")
        print("| 4 - Mostrar tareas.               |")
        print("| 5 - Salir.                        |")
        print("+-----------------------------------+\n")


def validar_opcion(msg_input: str, msg_error: str) -> int:
    """
    Funcion para verificar opcion de entrada

    Args:
        msg_input (str): Mensaje de input
        msg_error (str): Mensaje de error

    Return:
        (int): opcion validada
    """
    while True:
        try:
            opcion = input(msg_input)
            opcion = int(opcion)
            break
        except ValueError:
            print(msg_error)
    return opcion


def leer_cadenas(msg_imput: str, msg_error: str) -> str:
    """
    Función para verifcar el texto en formato correcto.
    Sin espacios y que no sea una cadena vacía.

    Args:
        msg_imput (str): Mensaje de input.
        msg_error (str): mensaje de error.

    Returns:
        str: texto con formato correcto.
    """
    while True:
        texto = input(msg_imput).lower()
        try:
            if not texto.strip():
                raise ValueError(msg_error)
        except ValueError as e:
            print(f"❌ ERROR: {e}")
        else:
            break
    return texto


def validacion_dato(msg_input: str, msg_error_neg: str, msg_error: str, tipo_dato: type):
    """
    Funció para validar datos

    Args:
        msg_input (str): Mensaje de input
        msg_error_neg (str): Mensaje de error, precio negativo.
        msg_error (str): Mensaje de error generico
        tipo_dato (_type_): Tipo de dato esperado.

    Returns:
        float: Dato con formato correcto de moneda
    """
    while True:
        dato = input(msg_input)
        try:
            dato = tipo_dato(dato)
            if dato < 0:
                print(msg_error_neg)
                continue
            break
        except ValueError:
            print(f"❌ ERROR: {msg_error}")
    return dato


def establecer_prioridad(msg_input_pr: str, msg_error_pr) -> str:
    """
    Función para validar la opción de prioriad

    Args:
        msg_input_pr (str): Input de prioridad.
        msg_error_str_pr (_type_): Mensaje de error.

    Returns:
        str: Valor de prioridad.
    """
    while True:
        prioridad = input(msg_input_pr).title()
        if prioridad == "Alta":
            return prioridad
        elif prioridad == "Media":
            return prioridad
        elif prioridad == "Baja":
            return prioridad
        else:
            print(msg_error_pr)


def mostrar_tareas(tareas_a_mostrar: list):
    """
    Función para mostrar las tareas.

    Args:
        tareas_a_mostrar (list): Lista de tareas a mostrar
    """
    print("Lista de tareas:")
    print("----------------------------------")
    # Si hay tareas en la lista
    if tareas_a_mostrar:
        # Recorremos la lista de tareas.
        for tarea in tareas_a_mostrar:
            # Establecer formato de prioridad
            prioridad = None
            if tarea['prioridad'] == "Alta":
                prioridad = "🔴 Alta"
            elif tarea['prioridad'] == "Media":
                prioridad = "🟡 Media"
            elif tarea['prioridad'] == "Baja":
                prioridad = "🟢 Baja"
            # Establecer formato de completado
            if tarea['completada']:
                completado = "✅ Completado"
            else:
                completado = "❌ Sin completar"
            print(f"Tarea: {tarea['id']}.")
            print(f" - Prioridad: {prioridad}.")
            print(f" - Descripcion: {tarea['descripcion']}.")
            print(f" - Compeltada: {completado}.")
            print("----------------------------------")
