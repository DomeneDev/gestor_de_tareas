from task_logic import agregar_tarea, obtener_tareas, completar_tarea, eliminar_tareas

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
        print("+-----------------------------------+")
        print("|  ✍ Gestor de tareas 1.0           |")
        print("+-----------------------------------+")
        print("| 1 - Agregar tarea.                |")
        print("| 2 - Completar tarea.              |")
        print("| 3 - Elminar tarea.                |")
        print("| 4 - Mostrar tareas.               |")
        print("| 5 - Salir.                        |")
        print("+-----------------------------------+\n")
        # Opción introducidad por el usuario
        opcion = int(input("👉Introduce una opción: "))
        # Evaluamos opcion y actuamos en consecuencia
        match opcion:
            case 1:  # Agregar tarea
                descripcion = input("Introduce la descripción de la tarea: \n")
                prioridad = input(
                    "Introduce priodidad de la tarea (Alta/Media/Baja): ").title()
                agregar_tarea(tareas, descripcion, prioridad)
                print("✅ Tarea añadida correctemente.\n")
            case 2:  # Completar tarea
                id_tarea = int(
                    input("Introduce el ID de la tarea a completar: "))
                if completar_tarea(tareas, id_tarea):
                    print(f"✅ Tarea con ID: {id_tarea} completada.\n")
                else:
                    print(f"📛 No existe la tarea con ID: {id_tarea}.\n")
            case 3:  # Eliminar tarea
                id_tarea = int(
                    input("Introduce el ID de la tarea a eliminar: "))
                if eliminar_tareas(tareas, id_tarea):
                    print(f"✅ Tarea con ID: {id_tarea} eliminada.\n")
                else:
                    print(f"📛 No existe la tarea con ID: {id_tarea}.\n")
            case 4:  # Mostrar tareas
                tareas_a_mostrar = obtener_tareas(tareas)
                print("Lista de tareas:")
                print("----------------------------------")
                # Si hay tareas en la lista
                if tareas_a_mostrar:
                    # Recorremos la lista de tareas.
                    for tarea in tareas:
                        # Establecer formato de prioridad
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
            case 5:
                print("🖐 Saliendo del programa....")
                break
            case _:
                print("❌ Opción no valida...")


if __name__ == "__main__":
    ejecutar_gestor_tareas()
