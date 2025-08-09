import random

class Proceso:
    def __init__(self, pid, nombre, ram, duracion, lectura_entrada):
        self.pid = pid
        self.nombre = nombre
        self.ram = ram
        self.duracion = duracion
        self.lectura_entrada = lectura_entrada

    def mostrar(self):
        print(f"PID: {self.pid} | Nombre: {self.nombre} | RAM: {self.ram}MB | "
              f"Duración: {self.duracion}s | Lectura Entrada: {'Sí' if self.lectura_entrada else 'No'}")

def generar_proceso_aleatorio(pid, nombres_disponibles, max_ram=1024):
    nombre = nombres_disponibles.pop(0)
    ram = random.randint(64, max_ram)  # Limita la RAM máxima
    duracion = random.randint(5, 9)
    lectura_entrada = random.choice([True, False])
    return Proceso(pid, nombre, ram, duracion, lectura_entrada)

if __name__ == "__main__":
    nombres_posibles = ["Chrome", "Photoshop", "Terminal", "EditorTexto", "Navegador", "Antivirus", "Word"]
    cantidad = min(7, len(nombres_posibles))  # No más procesos que nombres únicos
    procesos = []

    for i in range(1, cantidad + 1):
        proceso = generar_proceso_aleatorio(i, nombres_posibles)
        procesos.append(proceso)

    print("🧩 Procesos generados aleatoriamente:\n")
    for p in procesos:
        p.mostrar()