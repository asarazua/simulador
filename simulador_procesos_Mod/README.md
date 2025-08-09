# Simulador (Proceso) Descripción del Proyecto
Simulador de Procesos Grupo #3 Sistemas Operativos

El programa simula la gestión de procesos y la administración de memoria en un sistema operativo, permitiendo al usuario agregar procesos manualmente o generarlos automáticamente, y visualizando en tiempo real el uso de la memoria y el estado de los procesos mediante una interfaz gráfica

# Tecnologías Implementadas: 
  Lenguaje de programación: Python

Entorno de desarrollo: Visual Studio Code (VS Code)

Control de versiones: GitHub (para gestión del código y colaboración en equipo)

Librerías/Frameworks: importante threading

Sistema operativo: Principalmente en Windows.

# Instrucciones de instalación y uso: 
  Requisitos Previos
    Tener instalado Python 3.x (preferiblemente la última versión estable). Puedes descargarlo desde python.org.
    
    Tener instalado Git para clonar el repositorio (puedes realizarlo desde github en línea)
    
    (Opcional) Visual Studio Code para editar y ejecutar el código.

  Instalación
    Para comenzar, primero debes clonar el repositorio desde GitHub en tu computadora. Luego, accede a la carpeta del proyecto y, si deseas, crea un entorno virtual para manejar las dependencias de Python. Si el proyecto utiliza librerías externas, instálalas antes de ejecutar el programa.
  
  Para usar el simulador, simplemente ejecuta el archivo principal del programa. Puedes modificar los archivos para agregar o cambiar los procesos y ver cómo se gestionan en la simulación. El programa mostrará en pantalla el estado actual de la memoria y la cola de procesos.

# Capturas del funcionamiento del programa:
En la siguiente imagen se muestra la interfaz gráfica implementada con las restricciones indicadas:
<img width="498" height="403" alt="image" src="https://github.com/user-attachments/assets/75f81f0a-8180-40fd-8880-5dcf3a5777d9" />

En la siguiente imagen se muestra la determinación de procesos, el consumo de memoria RAM por proceso y la duración en segundos, el cual está esablecido en aleatorio entre 5 y 9 segundos.
También muestra los procesos en ejecución sin sobrepasar los 1024 MB.
Muestra los procesos que están en cola a espera de memoria para ejecutarse.
<img width="723" height="396" alt="image" src="https://github.com/user-attachments/assets/d319f081-c199-4640-9879-3fa96772b0e6" />

Al completar todos los procesos, se libera la memoria RAM y la simulación queda completada.
<img width="718" height="372" alt="image" src="https://github.com/user-attachments/assets/a783ce01-ba98-4f01-b393-37d07d45e33d" />



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








