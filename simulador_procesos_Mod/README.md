
# Simulador Ejecución.
1. proceso.py
Propósito: Define la clase Proceso y la función para generar procesos aleatorios.
Lógica esperada:
•
Clase Proceso: Representa un proceso con atributos como PID, nombre, cantidad de RAM requerida, duración de ejecución y si requiere lectura de entrada.
•
Función generar_proceso_aleatorio: Crea instancias de Proceso con valores aleatorios para simular diferentes tipos de procesos.
Ejemplo de estructura:
2. memoria.py
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
3. Simulador2.py (Interfaz gráfica y lógica principal)
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
Flujo General del Programa
1.
Inicio: El usuario abre la aplicación y ve la interfaz gráfica.
2.
Agregar procesos: El usuario puede agregar procesos manualmente (nombre, RAM, duración, lectura de entrada) o dejar que el simulador genere procesos aleatorios.
3.
Iniciar simulación: Al iniciar, los procesos se agregan a la cola de espera de la memoria.
4.
Ejecución de procesos: El AdministradorMemoria revisa la cola de espera y ejecuta procesos si hay suficiente memoria disponible, usando hilos para simular la concurrencia.
5.
Actualización de estado: La interfaz muestra en tiempo real la memoria usada, disponible, procesos en ejecución y en espera.
6.
Finalización: Cuando todos los procesos terminan, la simulación se da por completada.
Resumen
•
El programa simula la administración de procesos y memoria RAM, permitiendo observar cómo se asignan y ejecutan procesos en un entorno controlado.
•
Utiliza Kivy para la interfaz gráfica, facilitando la interacción y visualización.
•
Implementa concurrencia con hilos para simular la ejecución simultánea de procesos.
•
Permite experimentar con diferentes configuraciones de procesos y observar el impacto en el uso de la memoria.


