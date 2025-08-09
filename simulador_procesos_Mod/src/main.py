from src.simulador import Simulador
from src.memoria import Memoria
from src.proceso import Proceso

def cargar_procesos():
    cantidad = int(input("¿Cuántos procesos quieres simular? "))
    procesos = []

    for i in range(1, cantidad + 1):
        print(f"\n🔧 Proceso {i}")
        nombre = input(f"Nombre del proceso {i}: ")
        llegada = int(input("Tiempo de llegada: "))
        duracion = int(input("Duración: "))
        memoria = int(input("Memoria requerida (MB): "))
        lectura = input("¿Requiere lectura de entrada? (s/n): ").strip().lower()
        lectura_entrada = lectura == 's'

        proceso = Proceso(i, nombre, memoria, duracion, lectura_entrada)
        procesos.append(proceso)

    return procesos

def main():
    print("\n📊 SIMULADOR DE PLANIFICACIÓN DE PROCESOS")
    procesos = cargar_procesos()

    print("\n📋 Procesos ingresados manualmente:\n")
    for p in procesos:
        p.mostrar()

    memoria_total = int(input("\n🔍 Ingresa la memoria total disponible (MB): "))
    memoria = Memoria(memoria_total)
    simulador = Simulador(procesos, memoria)

    algoritmo = input("\n⚙️ Elige algoritmo (FCFS, SJF, RR): ").upper()

    if algoritmo == "FCFS":
        simulador.fcfs()
    elif algoritmo == "SJF":
        simulador.sjf()
    elif algoritmo == "RR":
        quantum = int(input("Ingresa el quantum: "))
        simulador.round_robin(quantum)
    else:
        print("❌ Algoritmo no reconocido.")

    simulador.mostrar_resultados()

if __name__ == "__main__":
    main()