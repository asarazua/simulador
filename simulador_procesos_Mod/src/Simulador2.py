import time
import threading
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.clock import Clock
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
            Clock.schedule_once(lambda dt: self.gui_callback(msg))
        try:
            time.sleep(proceso.duracion)
            if self.gui_callback:
                Clock.schedule_once(lambda dt: self.gui_callback(f"✔ {proceso.nombre} (PID:{proceso.pid}) COMPLETADO"))
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

class SimuladorGUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.memoria = AdministradorMemoria(1024, gui_callback=self.log)
        self.procesos = []
        self.pid = 1
        self.ejecutor = None
        self.actualizando = False

        self.estado_label = Label(text="", font_size=16, halign="left", valign="top", size_hint_y=None, height=80)
        self.add_widget(self.estado_label)

        self.log_text = TextInput(text="", readonly=True, size_hint_y=0.5, font_size=14)
        self.add_widget(self.log_text)

        btns = BoxLayout(size_hint_y=None, height=50)
        self.btn_agregar = Button(text="Agregar Proceso Manual")
        self.btn_agregar.bind(on_release=self.agregar_manual)
        btns.add_widget(self.btn_agregar)
        self.btn_iniciar = Button(text="Iniciar Simulación")
        self.btn_iniciar.bind(on_release=self.iniciar)
        btns.add_widget(self.btn_iniciar)
        self.add_widget(btns)

        Clock.schedule_once(lambda dt: self.actualizar_estado(), 0.5)

    def agregar_manual(self, instance):
        self.popup_proceso_manual()

    def popup_proceso_manual(self):
        layout = BoxLayout(orientation='vertical', spacing=5, padding=10)
        nombre_input = TextInput(hint_text="Nombre del proceso")
        ram_input = TextInput(hint_text="RAM requerida (MB)", input_filter='int')
        duracion_input = TextInput(hint_text="Duración (s)", input_filter='int')
        lectura_btn = Button(text="¿Lectura de entrada? (Presiona para alternar)", background_color=(0.7,0.7,1,1))
        lectura_estado = [False]
        def toggle_lectura(instance):
            lectura_estado[0] = not lectura_estado[0]
            lectura_btn.text = "Lectura de entrada: Sí" if lectura_estado[0] else "Lectura de entrada: No"
        lectura_btn.bind(on_release=toggle_lectura)
        layout.add_widget(nombre_input)
        layout.add_widget(ram_input)
        layout.add_widget(duracion_input)
        layout.add_widget(lectura_btn)
        btns = BoxLayout(size_hint_y=None, height=40)
        ok_btn = Button(text="Agregar")
        cancel_btn = Button(text="Cancelar")
        btns.add_widget(ok_btn)
        btns.add_widget(cancel_btn)
        layout.add_widget(btns)
        popup = Popup(title="Agregar Proceso Manual", content=layout, size_hint=(0.7, 0.6))

        def agregar(_):
            try:
                nombre = nombre_input.text.strip()
                ram = int(ram_input.text)
                duracion = int(duracion_input.text)
                if not nombre or ram <= 0 or duracion <= 0:
                    raise ValueError
                if ram > 1024:
                    self.log("❌ Error: La RAM solicitada excede el máximo permitido (1024 MB).")
                    return
                p = Proceso(self.pid, nombre, ram, duracion, lectura_estado[0])
                self.procesos.append(p)
                self.pid += 1
                self.log(f"➕ Proceso agregado: {p.nombre} (PID:{p.pid})")
                self.actualizar_estado()
                popup.dismiss()
            except Exception:
                self.log("❌ Error: Datos inválidos.")
        ok_btn.bind(on_release=agregar)
        cancel_btn.bind(on_release=lambda _: popup.dismiss())
        popup.open()

    def iniciar(self, instance):
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
            Clock.schedule_once(lambda dt: self.actualizar_estado(), 0.5)

    def actualizar_estado(self, *args):
        usada, total, disponible, ejec, espera = self.memoria.obtener_estado()
        estado = (
            f"MEMORIA: {usada}/{total}MB usada | {disponible}MB disponible\n"
            f"Procesos en ejecución: {ejec}\n"
            f"En cola de espera: {espera}"
        )
        self.estado_label.text = estado
        if self.ejecutor and not self.ejecutor.is_alive():
            self.actualizando = False
            self.log("🏁 SIMULACIÓN COMPLETADA")
        else:
            Clock.schedule_once(self.actualizar_estado, 1)

    def log(self, mensaje):
        self.log_text.text += mensaje + "\n"
        self.log_text.cursor = (0, len(self.log_text.text))

class SimuladorApp(App):
    def build(self):
        return SimuladorGUI()

if __name__ == "__main__":
    SimuladorApp().run()