import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
class Evento:
    """
    Clase que representa un evento o tarea dentro de la agenda.
    Cada objeto Evento almacena fecha, hora y descripción.
    """
    def __init__(self, fecha, hora, descripcion):
        self.fecha = fecha
        self.hora = hora
        self.descripcion = descripcion
    def obtener_datos(self):
        """
        Retorna los datos del evento en forma de tupla.
        """
        return self.fecha, self.hora, self.descripcion
class AgendaPersonalApp:
    """
    Clase principal de la aplicación.
    Se encarga de construir la interfaz gráfica y manejar las acciones
    del usuario como agregar, eliminar y visualizar eventos.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("820x550")
        self.root.resizable(False, False)
        self.lista_eventos = []
        self.crear_interfaz()
    def crear_interfaz(self):
        """
        Crea y organiza todos los componentes visuales de la aplicación.
        """
        self.frame_principal = tk.Frame(self.root, padx=15, pady=15)
        self.frame_principal.pack(fill="both", expand=True)
        self.label_titulo = tk.Label(
            self.frame_principal,
            text="Aplicación de Agenda Personal",
            font=("Arial", 18, "bold")
        )
        self.label_titulo.pack(pady=10)
        self.frame_entrada = tk.LabelFrame(
            self.frame_principal,
            text="Datos del evento o tarea",
            padx=10,
            pady=10
        )
        self.frame_entrada.pack(fill="x", pady=10)
        self.label_fecha = tk.Label(self.frame_entrada, text="Fecha:")
        self.label_fecha.grid(row=0, column=0, padx=8, pady=8, sticky="w")
        self.date_picker = DateEntry(
            self.frame_entrada,
            width=18,
            date_pattern="yyyy-mm-dd",
            background="darkblue",
            foreground="white",
            borderwidth=2
        )
        self.date_picker.grid(row=0, column=1, padx=8, pady=8, sticky="w")
        self.label_hora = tk.Label(self.frame_entrada, text="Hora (HH:MM):")
        self.label_hora.grid(row=0, column=2, padx=8, pady=8, sticky="w")
        self.entry_hora = tk.Entry(self.frame_entrada, width=20)
        self.entry_hora.grid(row=0, column=3, padx=8, pady=8, sticky="w")
        self.label_descripcion = tk.Label(self.frame_entrada, text="Descripción:")
        self.label_descripcion.grid(row=1, column=0, padx=8, pady=8, sticky="w")
        self.entry_descripcion = tk.Entry(self.frame_entrada, width=60)
        self.entry_descripcion.grid(row=1, column=1, columnspan=3, padx=8, pady=8, sticky="w")
        self.frame_botones = tk.Frame(self.frame_principal)
        self.frame_botones.pack(fill="x", pady=10)
        self.boton_agregar = tk.Button(
            self.frame_botones,
            text="Agregar Evento",
            width=18,
            command=self.agregar_evento
        )
        self.boton_agregar.pack(side="left", padx=5)
        self.boton_eliminar = tk.Button(
            self.frame_botones,
            text="Eliminar Evento Seleccionado",
            width=25,
            command=self.eliminar_evento
        )
        self.boton_eliminar.pack(side="left", padx=5)
        self.boton_salir = tk.Button(
            self.frame_botones,
            text="Salir",
            width=12,
            command=self.salir_aplicacion
        )
        self.boton_salir.pack(side="right", padx=5)
        self.frame_lista = tk.LabelFrame(
            self.frame_principal,
            text="Eventos programados",
            padx=10,
            pady=10
        )
        self.frame_lista.pack(fill="both", expand=True, pady=10)
        columnas = ("Fecha", "Hora", "Descripción")
        self.tree_eventos = ttk.Treeview(
            self.frame_lista,
            columns=columnas,
            show="headings",
            height=14
        )
        self.tree_eventos.heading("Fecha", text="Fecha")
        self.tree_eventos.heading("Hora", text="Hora")
        self.tree_eventos.heading("Descripción", text="Descripción")
        self.tree_eventos.column("Fecha", width=140, anchor="center")
        self.tree_eventos.column("Hora", width=100, anchor="center")
        self.tree_eventos.column("Descripción", width=500, anchor="w")
        self.scroll_y = ttk.Scrollbar(
            self.frame_lista,
            orient="vertical",
            command=self.tree_eventos.yview
        )
        self.tree_eventos.configure(yscrollcommand=self.scroll_y.set)
        self.tree_eventos.pack(side="left", fill="both", expand=True)
        self.scroll_y.pack(side="right", fill="y")
    def validar_hora(self, hora):
        """
        Valida que la hora esté en formato HH:MM
        y que sus valores sean correctos.
        """
        try:
            partes = hora.split(":")
            if len(partes) != 2:
                return False
            horas = int(partes[0])
            minutos = int(partes[1])
            if 0 <= horas <= 23 and 0 <= minutos <= 59:
                return True
            return False
        except ValueError:
            return False
    def agregar_evento(self):
        """
        Agrega un nuevo evento a la lista interna y al Treeview.
        También valida que los datos sean correctos antes de agregar.
        """
        fecha = self.date_picker.get().strip()
        hora = self.entry_hora.get().strip()
        descripcion = self.entry_descripcion.get().strip()
        if not fecha or not hora or not descripcion:
            messagebox.showwarning(
                "Campos incompletos",
                "Debe completar la fecha, la hora y la descripción."
            )
            return
        if not self.validar_hora(hora):
            messagebox.showerror(
                "Hora inválida",
                "Ingrese una hora válida en formato HH:MM."
            )
            return
        nuevo_evento = Evento(fecha, hora, descripcion)
        self.lista_eventos.append(nuevo_evento)
        self.tree_eventos.insert("", "end", values=nuevo_evento.obtener_datos())
        self.entry_hora.delete(0, tk.END)
        self.entry_descripcion.delete(0, tk.END)
        messagebox.showinfo("Éxito", "Evento agregado correctamente.")
    def eliminar_evento(self):
        """
        Elimina el evento seleccionado tanto del Treeview
        como de la lista interna de eventos.
        """
        seleccion = self.tree_eventos.selection()
        if not seleccion:
            messagebox.showwarning(
                "Sin selección",
                "Debe seleccionar un evento para eliminar."
            )
            return
        confirmar = messagebox.askyesno(
            "Confirmar eliminación",
            "¿Está seguro de eliminar el evento seleccionado?"
        )
        if confirmar:
            item = seleccion[0]
            valores_item = self.tree_eventos.item(item, "values")
            self.tree_eventos.delete(item)
            for evento in self.lista_eventos:
                if evento.obtener_datos() == valores_item:
                    self.lista_eventos.remove(evento)
                    break
            messagebox.showinfo("Eliminado", "Evento eliminado correctamente.")
    def salir_aplicacion(self):
        """
        Cierra la aplicación.
        """
        self.root.quit()
if __name__ == "__main__":
    ventana = tk.Tk()
    app = AgendaPersonalApp(ventana)
    ventana.mainloop()