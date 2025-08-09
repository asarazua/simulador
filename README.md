
# Simulador
Simulador de Procesos Grupo #3 Sistemas Operativos

# La estructura en el repositorio
Cuenta con una rama principal en la cual está contenido todo el proyecto.
Dentro encontramos la carpeta simulador_procesos_Mod en donde encontramos un Readme.md de entrada con la descripción general del proceso
y la carpeta denominada src (origen) que contiene todos los archivos del programa.

# Simulador de Procesos (Descripción)

Este proyecto simula procesos del sistema operativo, generando características como PID, nombre, uso de RAM, duración y si requieren lectura de entrada. Los procesos se crean de forma aleatoria para representar una carga variada del sistema cuando se ejecuta en automático, aunque cuenta con la opción de ejecutar procesos de forma manual a elección del usuario, cuenta con una interfaz gráfica para 
una experiencia más amigable con el usuario.

## Tecnologías utilizadas

- Python 3.x
- Visual Studio Code
- PowerShell o terminal integrada
- Módulos estándar (`random`, `os`, etc.)

## Funcionalidades completadas

- Creación de procesos con atributos aleatorios
- Impresión estructurada de procesos generados
- Organización en clases (`Proceso`) y ejecución en `simulador.py`

## Requisitos
- Python 3.10 o superior

## Cómo ejecutar el simulador

1. Clona el repositorio o abre la carpeta en VS Code
2. Ve a la terminal y escribe:

```bash
cd src
python simulador.py
(Versión inicial con arquitectura base y clase Memoria)
