import time
import threading
from proceso import Proceso, generar_proceso_aleatorio

class AdministradorMemoria:
    def __init__(self, capacidad):
        self.capacidad = capacidad  # MB
        self.usada = 0
        self.lock = threading.Lock()
        self.procesos_en_ejecucion = []  # [(Proceso, Thread)]
        self.cola_espera = []            # [Proceso]
        self.activo = True

    def agregar_proceso(self, proceso):
        with self.lock:
            self.cola_espera.append(proceso)

    def agregar_procesos(self, procesos):
        with self.lock:
            self.cola_espera.extend(procesos)

    def ejecutar(self):
        while True:
            with self.lock:
                i = 0
                while i < len(self.cola_espera):
                    proceso = self.cola_espera[i]
                    if self.usada + proceso.ram <= self.capacidad:
                        self.usada += proceso.ram
                        hilo = threading.Thread(target=self._ejecutar_proceso, args=(proceso,))
                        hilo.start()
                        self.procesos_en_ejecucion.append((proceso, hilo))
                        self.cola_espera.pop(i)
                    else:
                        i += 1
                # Si no hay procesos en ejecución ni en cola, terminar ciclo
                if not self.procesos_en_ejecucion and not self.cola_espera:
                    break
            time.sleep(0.2)

    def _ejecutar_proceso(self, proceso):
        print(f"⚡ {proceso.nombre} (PID:{proceso.pid}) INICIADO: RAM {proceso.ram}MB, Duración {proceso.duracion}s")

        try:
            time.sleep(proceso.duracion)
            print(f"✔ {proceso.nombre} (PID:{proceso.pid}) COMPLETADO")
        finally:
            with self.lock:
                self.usada -= proceso.ram
                self.procesos_en_ejecucion = [
                    (p, h) for (p, h) in self.procesos_en_ejecucion if p.pid != proceso.pid
                ]
                

    def mostrar_estado(self):
        with self.lock:
            print("\n" + "="*50)
            print(f"MEMORIA: {self.usada}/{self.capacidad}MB usada")
            print(f"Procesos en ejecución: {[p.nombre for (p, _) in self.procesos_en_ejecucion]}")
            print(f"En cola de espera: {[p.nombre for p in self.cola_espera]}")
            print("="*50)

    def detener(self):
        self.activo = False

def crear_proceso_manual(pid):
    while True:
        nombre = input("Nombre del proceso: ")
        ram = int(input("RAM requerida (MB): "))
        if ram > 1024:
            print("❌ Error: La RAM solicitada excede el máximo permitido (1024 MB). Intente de nuevo.")
            continue
        duracion = int(input("Duración (s): "))
        lectura_entrada = input("¿Lectura de entrada? (s/n): ").strip().lower() == "s"
        return Proceso(pid, nombre, ram, duracion, lectura_entrada)

def simulador():
    nombres_posibles = ["Chrome", "Photoshop", "Terminal", "EditorTexto", "Navegador", "Antivirus", "Word"]
    memoria = AdministradorMemoria(1024)
    procesos = []
    pid = 1

    print("¿Desea agregar procesos manualmente? (s/n): ", end="")
    if input().strip().lower() == "s":
        while True:
            procesos.append(crear_proceso_manual(pid))
            pid += 1
            print("¿Agregar otro proceso? (s/n): ", end="")
            if input().strip().lower() != "s":
                break
    else:
        cantidad = min(7, len(nombres_posibles))
        nombres_copia = nombres_posibles.copy()
        procesos = [generar_proceso_aleatorio(i, nombres_copia, memoria.capacidad) for i in range(1, cantidad + 1)]

    print("⚡ PROCESOS GENERADOS:")
    for p in procesos:
        print(f"- {p.nombre} (PID:{p.pid}): {p.ram}MB por {p.duracion}s")
    memoria.agregar_procesos(procesos)
    ejecutor = threading.Thread(target=memoria.ejecutar)
    ejecutor.start()
    try:
        while ejecutor.is_alive():
            memoria.mostrar_estado()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n✖ Detenido por usuario")
        memoria.detener()
    finally:
        ejecutor.join()
        memoria.mostrar_estado()
        print("\n🏁 SIMULACIÓN COMPLETADA")

if __name__ == "__main__":
    simulador()