# 📝 TaskMaster Pro: Gestor de Tareas con Prioridades

Aplicación de consola diseñada para la gestión eficiente de tareas pendientes, permitiendo clasificar actividades por niveles de urgencia y gestionar su estado de cumplimiento.

## 🚀 Características

- **Gestión Dinámica**: Alta, baja y visualización de tareas en tiempo real.
- **Sistema de Prioridades**: Clasificación por niveles (Alta, Media, Baja).
- **Control de Estados**: Marcado de tareas como pendientes o completadas.

## 📂 Estructura del Proyecto

```plaintext
task_master/
├── main.py              # Orquestador del programa y menú match-case.
├── task_logic.py        # Motor de gestión de la lista de tareas.
└── README.md            # Documentación del proyecto.
🛠️ Instalación y Uso
Asegúrate de tener instalado Python 3.10 o superior.

Ejecuta el programa principal:

Bash

python main.py
🛡️ Roadmap de Aprendizaje (Sprints)
[ ] Sprint 1: Lógica Core

CRUD básico de tareas (Crear, Leer, Eliminar) usando listas de diccionarios.

[ ] Sprint 2: Robustez y Validación

Control de errores en la entrada de prioridades y selección de IDs.

[ ] Sprint 3: Refactorización Arquitectónica (Utils)

Aplicación de la Navaja de Ockham: Separación de UI y utilidades.

[ ] Sprint 4: Persistencia de Datos

Guardado automático y carga desde archivo CSV.

[ ] Sprint 5: Paradigma de Objetos (POO)

Transformación a clases Task y TaskManager.
```
