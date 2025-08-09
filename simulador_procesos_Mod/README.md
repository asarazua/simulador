# Simulador (Proceso) Descripción del Proyecto
Simulador de Procesos Grupo #3 Sistemas Operativos

El programa simula la gestión de procesos y la administración de memoria en un sistema operativo, permitiendo al usuario agregar procesos manualmente o generarlos automáticamente, y visualizando en tiempo real el uso de la memoria y el estado de los procesos mediante una interfaz gráfica

# Tecnologías Implementadas: 
  Para elaboración de este proyecto se utilizó el lenguaje de programación Python.
  Para editor de código se utilizó VS Code.
  El proyecto se subió a Github en un repositorio público

# Tecnologías Implementadas: 
  Lenguaje de programación: Python

Entorno de desarrollo: Visual Studio Code (VS Code)

Control de versiones: Git y GitHub (para gestión del código y colaboración en equipo)

Librerías/Frameworks (si aplicaste alguna):

Por ejemplo, si usaste alguna librería como threading, multiprocessing, psutil u otra, aquí la mencionas.

Sistema operativo: (opcional) Indica si desarrollaste principalmente en Windows, Linux o macOS

## 1. Proceso.py

  Propósito: Define la clase Proceso y la función para generar procesos aleatorios.
  
  Lógica esperada:
    •
    Clase Proceso: Representa un proceso con atributos como PID, nombre, cantidad de RAM requerida, duración de ejecución y si requiere    lectura de entrada.
    •
    Función generar_proceso_aleatorio: Crea instancias de Proceso con valores aleatorios para simular diferentes tipos de procesos.
    
    Ejemplo de estructura:
<img width="662" height="238" alt="image" src="https://github.com/user-attachments/assets/0df2e168-0631-4daa-a8ac-5c11a493aa70" />

   
# 2. Memoria.py

  Propósito: Gestiona la memoria RAM disponible y la asignación de procesos a la memoria.
  Lógica esperada:
    •
    Clase AdministradorMemoria:
    o
    Controla la cantidad de memoria usada y disponible.
    o
    Mantiene listas de procesos en ejecución y en espera.
    o
    Permite agregar procesos a la cola de espera.
    o
    Ejecuta procesos si hay suficiente memoria disponible, usando hilos para simular la ejecución concurrente.
    o
    Libera memoria cuando un proceso termina.
    o
    Proporciona el estado actual de la memoria y los procesos.
    
    Ejemplo de estructura:

<img width="629" height="314" alt="image" src="https://github.com/user-attachments/assets/db6035f0-65d5-4bf2-971d-3aede639f405" />


## Simulador.py

  Propósito: Proporciona la interfaz gráfica y conecta la lógica de procesos y memoria.
  Lógica:
    •
    Clase SimuladorGUI:
    o
    Permite agregar procesos manualmente mediante un formulario.
    o
    Permite iniciar la simulación, generando procesos automáticos si no hay procesos manuales.
    o
    Muestra el estado de la memoria, los procesos en ejecución y en espera.
    o
    Muestra un log de eventos importantes (inicio, finalización de procesos, errores).
    o
    Actualiza la interfaz en tiempo real usando el reloj de Kivy.
    •
    Clase SimuladorApp:
    o
    Inicializa y ejecuta la aplicación Kivy.

<img width="643" height="365" alt="image" src="https://github.com/user-attachments/assets/a23139fa-febb-4717-853f-12cd1597a79f" />






