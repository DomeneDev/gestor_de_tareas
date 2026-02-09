from task_logic import agregar_tarea, obtener_tareas, completar_tarea, eliminar_tareas
from utils import mostrar_menu, validar_opcion, leer_cadenas, validacion_dato, establecer_prioridad, mostrar_tareas


# ----  CONSTANTES PARA INPUTS ----
INPUT_OPC = "👉Introduce una opción: "
INPUT_DESC = "Introduce la descripción de la tarea: "
INPUT_PR = "Introduce la prioridad (Alta/Media/Baja): "
INPUT_ID = "Introduce el ID de la tarea a completar: "

# ---- COSNTANTES PARA ERROR ----
ERROR_OPC = "🛑 El valor introducido debe ser un número entero"
ERROR_DESC = "🛑 No has introducido un nombre válido.."
ERROR_PR = "🛑 Introduce una prioridad válida."
ERROR_ID_NEG = "🛑 Una tarea no puede tener un ID negativo..."
ERROR_ID = "🛑 Introduce un valor válido (numero entero)."


# Bucle principal del programa


def ejecutar_gestor_tareas():
    """
    Función para ejecutar el programa y su funcionalidad.
    """
    # Lista para almacenar las tareas
    tareas = []
    # Bucle principal del programa
    while True:
        # Menu de acciones de la app
        mostrar_menu()
        # Opción introducidad por el usuario
        opcion = validar_opcion(INPUT_OPC, ERROR_OPC)
        # Evaluamos opcion y actuamos en consecuencia
        match opcion:
            case 1:  # Agregar tarea
                descripcion = leer_cadenas(INPUT_DESC, ERROR_DESC)
                prioridad = establecer_prioridad(INPUT_PR, ERROR_PR)
                agregar_tarea(tareas, descripcion, prioridad)
                print("✅ Tarea añadida correctemente.\n")
            case 2:  # Completar tarea
                id_tarea = validacion_dato(
                    INPUT_ID, ERROR_ID_NEG, ERROR_ID, int)
                if completar_tarea(tareas, id_tarea):
                    print(f"✅ Tarea con ID: {id_tarea} completada.\n")
                else:
                    print(
                        f"📛 No existe la tarea con ID: {id_tarea}.\n")
            case 3:  # Eliminar tarea
                while True:
                    id_tarea = validacion_dato(
                        INPUT_ID, ERROR_ID_NEG, ERROR_ID, int)
                    if eliminar_tareas(tareas, id_tarea):
                        print(f"✅ Tarea con ID: {id_tarea} eliminada.\n")
                    else:
                        print(
                            f"📛 No existe la tarea con ID: {id_tarea}.\n")
            case 4:  # Mostrar tareas
                tareas_a_mostrar = obtener_tareas(tareas)
                mostrar_tareas(tareas_a_mostrar)
            case 5:
                print("🖐 Saliendo del programa....")
                break
            case _:
                print("❌ Opción no valida...")


if __name__ == "__main__":
    ejecutar_gestor_tareas()
