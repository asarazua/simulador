import time
import threading
import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext
from proceso import Proceso, generar_proceso_aleatorio

class AdministradorMemoria:
    def __init__(self, capacidad, gui_callback=None):
        self.capacidad = capacidad  # MB
        self.usada = 0
        self.lock = threading.Lock()
        self.procesos_en_ejecucion = []  # [(Proceso, Thread)]
        self.cola_espera = []            # [Proceso]
        self.activo = True
        self.gui_callback = gui_callback

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
                if not self.procesos_en_ejecucion and not self.cola_espera:
                    break
            time.sleep(0.2)

    def _ejecutar_proceso(self, proceso):
        msg = f"⚡ {proceso.nombre} (PID:{proceso.pid}) INICIADO: RAM {proceso.ram}MB, Duración {proceso.duracion}s"
        if proceso.lectura_entrada:
            msg += " | 🔵 Esperando entrada de usuario..."
        if self.gui_callback:
            self.gui_callback(msg)
        try:
            time.sleep(proceso.duracion)
            if self.gui_callback:
                self.gui_callback(f"✔ {proceso.nombre} (PID:{proceso.pid}) COMPLETADO")
        finally:
            with self.lock:
                self.usada -= proceso.ram
                self.procesos_en_ejecucion = [
                    (p, h) for (p, h) in self.procesos_en_ejecucion if p.pid != proceso.pid
                ]

    def obtener_estado(self):
        with self.lock:
            disponible = self.capacidad - self.usada
            ejec = [p.nombre for (p, _) in self.procesos_en_ejecucion]
            espera = [p.nombre for p in self.cola_espera]
            return self.usada, self.capacidad, disponible, ejec, espera

def crear_proceso_manual(pid, root):
    while True:
        nombre = simpledialog.askstring("Nuevo Proceso", "Nombre del proceso:", parent=root)
        if nombre is None:
            return None
        try:
            ram = int(simpledialog.askstring("Nuevo Proceso", "RAM requerida (MB):", parent=root))
        except:
            continue
        if ram > 1024:
            messagebox.showerror("Error", "La RAM solicitada excede el máximo permitido (1024 MB).")
            continue
        try:
            duracion = int(simpledialog.askstring("Nuevo Proceso", "Duración (s):", parent=root))
        except:
            continue
        lectura_entrada = messagebox.askyesno("Lectura de entrada", "¿Lectura de entrada?")
        return Proceso(pid, nombre, ram, duracion, lectura_entrada)

class SimuladorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Procesos - Memoria")
        self.text_estado = tk.Label(root, text="", font=("Consolas", 12), justify="left")
        self.text_estado.pack(padx=10, pady=10)
        self.text_log = scrolledtext.ScrolledText(root, width=60, height=10, state="disabled", font=("Consolas", 10))
        self.text_log.pack(padx=10, pady=10)
        self.btn_agregar = tk.Button(root, text="Agregar Proceso Manual", command=self.agregar_manual)
        self.btn_agregar.pack(pady=5)
        self.btn_iniciar = tk.Button(root, text="Iniciar Simulación", command=self.iniciar)
        self.btn_iniciar.pack(pady=5)
        self.memoria = AdministradorMemoria(1024, gui_callback=self.log)
        self.procesos = []
        self.pid = 1
        self.ejecutor = None
        self.actualizando = False

    def agregar_manual(self):
        p = crear_proceso_manual(self.pid, self.root)
        if p:
            self.procesos.append(p)
            self.pid += 1
            self.log(f"➕ Proceso agregado: {p.nombre} (PID:{p.pid})")
            self.actualizar_estado()

    def iniciar(self):
        if not self.procesos:
            # Si no hay procesos manuales, genera automáticos
            nombres_posibles = ["Chrome", "Photoshop", "Terminal", "EditorTexto", "Navegador", "Antivirus", "Word"]
            cantidad = min(7, len(nombres_posibles))
            nombres_copia = nombres_posibles.copy()
            self.procesos = [generar_proceso_aleatorio(i, nombres_copia, self.memoria.capacidad) for i in range(1, cantidad + 1)]
            for p in self.procesos:
                self.log(f"➕ Proceso generado: {p.nombre} (PID:{p.pid})")
        self.memoria.agregar_procesos(self.procesos)
        self.ejecutor = threading.Thread(target=self.memoria.ejecutar)
        self.ejecutor.start()
        if not self.actualizando:
            self.actualizando = True
            self.root.after(500, self.actualizar_estado)

    def actualizar_estado(self):
        usada, total, disponible, ejec, espera = self.memoria.obtener_estado()
        estado = (
            f"MEMORIA: {usada}/{total}MB usada | {disponible}MB disponible\n"
            f"Procesos en ejecución: {ejec}\n"
            f"En cola de espera: {espera}"
        )
        self.text_estado.config(text=estado)
        if self.ejecutor and not self.ejecutor.is_alive():
            self.actualizando = False
            self.log("🏁 SIMULACIÓN COMPLETADA")
        else:
            self.root.after(1000, self.actualizar_estado)

    def log(self, mensaje):
        self.text_log.config(state="normal")
        self.text_log.insert(tk.END, mensaje + "\n")
        self.text_log.see(tk.END)
        self.text_log.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimuladorGUI(root)
    root.mainloop()