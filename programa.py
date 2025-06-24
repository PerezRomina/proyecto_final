import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("CONTROL ASISTENCIAS HOSPITAL")
        self.root.config(bg="lightblue")
        self.root.geometry("900x600")

        self.datos_trabajadores = []
        self.turnos = []
        self.faltas_registradas = {}
        self.periodos_vacacionales = {}
        self.horarios_guardados = {}

        self.menu_lateral = tk.Frame(self.root, bg="light salmon", width=150)
        self.menu_lateral.pack(side="left", fill="y")

        self.area_dinamica = tk.Frame(self.root, bg="bisque")
        self.area_dinamica.pack(side="right", expand=True, fill="both")

        self.crear_menu()
        self.saludo()

    def crear_menu(self):
        botones = [
            ("📌INICIO", self.saludo),
            ("📃REGISTRO", self.trabajador),
            ("TURNO", self.turno),
            ("HORARIOS", self.horarios),
            ("🏢FALTAS", self.faltas),
            ("PERIODO VACACIONAL", self.periodo_vacacional),
            ("IMPRESIÓN DE DATOS", self.imprimir)
        ]
        for texto, comando in botones:
            tk.Button(self.menu_lateral, text=texto, font="Times 14 bold", command=comando, width=20).pack(pady=10)

    def limpiar_area_dinamica(self):
        for widget in self.area_dinamica.winfo_children():
            widget.destroy()

    def saludo(self):
        self.limpiar_area_dinamica()
        tk.Label(self.area_dinamica, text="Bienvenido al sistema de asistencia",bg="#FFE4C4", font=("Courier New", 18)).pack(pady=10)
        tk.Button(self.area_dinamica, text="Bienvenida",
                  command=lambda: messagebox.showinfo("Bienvenido", "Buen día, bienvenido a la página oficial del hospital")).pack()

    def trabajador(self):
        self.limpiar_area_dinamica()
        tk.Label(self.area_dinamica, text="REGISTRO DE DATOS DEL TRABAJADOR",bg="#FFE4C4", font=("Courier New", 18)).pack(pady=10)

        campos = {}
        for etiqueta in ["Nombre", "Edad", "Número de trabajador", "Teléfono", "Correo electrónico"]:
            tk.Label(self.area_dinamica, text=f"{etiqueta}:").pack()
            entrada = tk.Entry(self.area_dinamica)
            entrada.pack()
            campos[etiqueta] = entrada

        tk.Label(self.area_dinamica, text="Género:").pack()
        genero_combo = ttk.Combobox(self.area_dinamica, values=["Masculino", "Femenino"])
        genero_combo.pack()

        tk.Label(self.area_dinamica, text="Puesto:").pack()
        puesto_combo = ttk.Combobox(self.area_dinamica, values=["Medico", "Pediatra", "Doctor", "Recepcionista"])
        puesto_combo.pack()

        def guardar_datos():
            numero = campos["Número de trabajador"].get()
            edad = campos["Edad"].get()
            telefono = campos["Teléfono"].get()

            if not numero.isdigit():
                messagebox.showerror("Error", "El número de trabajador debe ser numérico.")
                return
            if not edad.isdigit():
                messagebox.showerror("Error", "La edad debe ser numérica.")
                return
            if not telefono.isdigit() or len(telefono) < 7:
                messagebox.showerror("Error", "Número de teléfono inválido.")
                return

            datos = {
                "nombre": campos["Nombre"].get(),
                "edad": edad,
                "numero_trabajador": numero,
                "genero": genero_combo.get(),
                "puesto": puesto_combo.get(),
                "telefono": telefono,
                "correo": campos["Correo electrónico"].get()
            }

            if not all(datos.values()):
                messagebox.showwarning("Campos incompletos", "Por favor completa todos los campos.")
                return

            for trabajador in self.datos_trabajadores:
                if trabajador["numero_trabajador"] == numero:
                    messagebox.showwarning("Error", "Ya existe un trabajador con ese número.")
                    return

            self.datos_trabajadores.append(datos)
            messagebox.showinfo("Registro exitoso", "Datos guardados correctamente")

        tk.Button(self.area_dinamica, text="Guardar", command=guardar_datos, bg="pink").pack(pady=10)

    def turno(self):
        self.limpiar_area_dinamica()
        tk.Label(self.area_dinamica, text="TURNO DEL TRABAJADOR",bg="#FFE4C4", font=("Courier New", 18)).pack(pady=10)

        tk.Label(self.area_dinamica, text="Número de trabajador:").pack()
        num_trab_entry = tk.Entry(self.area_dinamica)
        num_trab_entry.pack()

        tk.Label(self.area_dinamica, text="Selecciona el turno:").pack()
        turno_combo = ttk.Combobox(self.area_dinamica, values=["Matutino", "Vespertino", "Nocturno"])
        turno_combo.pack()

        def guardar_turno():
            numero = num_trab_entry.get()
            turno = turno_combo.get()

            if not numero or not turno:
                messagebox.showwarning("Campos incompletos", "Completa todos los campos")
                return

            anterior = next((t["turno"] for t in self.turnos if t["numero_trabajador"] == numero), None)
            self.turnos = [t for t in self.turnos if t["numero_trabajador"] != numero]
            self.turnos.append({"numero_trabajador": numero, "turno": turno})

            mensaje = f"Turno actualizado de '{anterior}' a '{turno}'" if anterior else f"Turno '{turno}' asignado al trabajador {numero}"
            messagebox.showinfo("Turno guardado", mensaje)

        tk.Button(self.area_dinamica, text="Guardar turno", command=guardar_turno, bg="pink").pack(pady=18)

    def horarios(self):
        self.limpiar_area_dinamica()
        tk.Label(self.area_dinamica, text="HORARIOS DE TRABAJO",bg="#FFE4C4", font=("Courier New", 18)).pack(pady=10)

        texto = (
            "-Horarios por turno:\n"
            "-MATUTINO: 07:00 am - 03:00 pm\n"
            "-VESPERTINO: 03:00 pm - 11:00 pm\n"
            "-NOCTURNO: 11:00 pm - 07:00 am\n"
        )
        tk.Label(self.area_dinamica, text=texto, font=("Arial", 11), justify="left").pack(padx=20, pady=10)

        tk.Label(self.area_dinamica, text="Número de trabajador:").pack()
        num_trab_entry = tk.Entry(self.area_dinamica)
        num_trab_entry.pack()

        tk.Label(self.area_dinamica, text="Selecciona el horario correspondiente:").pack()
        horario_combo = ttk.Combobox(self.area_dinamica, values=[
            "07:00 am - 03:00 pm",
            "03:00 pm - 11:00 pm",
            "11:00 pm - 07:00 am"
        ])
        horario_combo.pack()

        def guardar_horario():
            numero = num_trab_entry.get()
            horario = horario_combo.get()

            if not numero.isdigit():
                messagebox.showerror("Error", "Número de trabajador inválido")
                return

            if numero not in [t["numero_trabajador"] for t in self.datos_trabajadores]:
                messagebox.showerror("No existe", "Este trabajador no está registrado")
                return

            if not horario:
                messagebox.showerror("Error", "Selecciona un horario correspondiente")
                return

            turno = next((t["turno"] for t in self.turnos if t["numero_trabajador"] == numero), None)
            turno_horario = {
                "Matutino": "07:00 am - 03:00 pm",
                "Vespertino": "03:00 pm - 11:00 pm",
                "Nocturno": "11:00 pm - 07:00 am"
            }

            if turno and turno_horario.get(turno) != horario:
                messagebox.showerror("HORARIO NO CORRESPONDIDO AL TURNO", f"El turno asignado es '{turno}' y el horario  debe ser '{turno_horario[turno]}'")
                return

            self.horarios_guardados[numero] = horario
            messagebox.showinfo("Horario guardado", f"Horario '{horario}' registrado para el trabajador {numero}")

        tk.Button(self.area_dinamica, text="Guardar horario", command=guardar_horario, bg="pink").pack(pady=10)

    def faltas(self):
        self.limpiar_area_dinamica()
        tk.Label(self.area_dinamica, text="REGISTRO DE FALTAS", bg="#FFE4C4", font=("Courier New", 18)).pack(pady=10)

        tk.Label(self.area_dinamica, text="Número de trabajador:").pack()
        num_trab_entry = tk.Entry(self.area_dinamica)
        num_trab_entry.pack()

        tk.Label(self.area_dinamica, text="Selecciona la cantidad de faltas:").pack()
        faltas_combo = ttk.Combobox(self.area_dinamica, values=["0 días", "1 día", "2 días", "3 días", "4 días", "5 días"])
        faltas_combo.pack()

        def registrar_falta():
            numero = num_trab_entry.get()
            faltas_str = faltas_combo.get()

            if not numero.isdigit():
                messagebox.showerror("Error", "Número de trabajador inválido")
                return

            if numero not in [t["numero_trabajador"] for t in self.datos_trabajadores]:
                messagebox.showerror("No existe", "Este trabajador no está registrado")
                return

            try:
                faltas_num = int(faltas_str.split()[0])
            except:
                messagebox.showerror("Error", "Selecciona una cantidad válida de faltas")
                return

            self.faltas_registradas[numero] = self.faltas_registradas.get(numero, 0) + faltas_num
            messagebox.showinfo("Falta registrada", f"{faltas_num} falta(s) registrada(s) para el trabajador {numero}")

        tk.Button(self.area_dinamica, text="Registrar falta", command=registrar_falta, bg="pink").pack(pady=10)

    def periodo_vacacional(self):
        self.limpiar_area_dinamica()
        tk.Label(self.area_dinamica, text="PERIODO VACACIONAL", bg="#FFE4C4", font=("Courier New", 18)).pack(pady=10)
        tk.Label(self.area_dinamica, text="Número de trabajador:").pack()
        num_trab_entry = tk.Entry(self.area_dinamica)
        num_trab_entry.pack()

        tk.Label(self.area_dinamica, text="Selecciona el periodo vacacional:").pack()
        periodo_combo = ttk.Combobox(self.area_dinamica, values=[
            "Enero-Febrero", "Febrero-Marzo", "Marzo-Abril", "Abril-Mayo", "Mayo-Junio",
            "Junio-Julio", "Julio-Agosto", "Agosto-Septiembre", "Septiembre-Octubre",
            "Octubre-Noviembre", "Noviembre-Diciembre"
        ])
        periodo_combo.pack()

        def guardar_periodo():
            numero = num_trab_entry.get()
            periodo = periodo_combo.get()

            if not numero.isdigit():
                messagebox.showerror("Error", "Número de trabajador inválido")
                return

            if numero not in [t["numero_trabajador"] for t in self.datos_trabajadores]:
                messagebox.showerror("No existe", "Este trabajador no está registrado")
                return

            if not periodo:
                messagebox.showwarning("Campos incompletos", "Selecciona un periodo vacacional")
                return

            self.periodos_vacacionales[numero] = periodo
            messagebox.showinfo("Periodo guardado", f"Periodo vacacional '{periodo}' asignado al trabajador {numero}")

        tk.Button(self.area_dinamica, text="Guardar periodo vacacional", command=guardar_periodo, bg="pink").pack(pady=10)

    def imprimir(self):
        self.limpiar_area_dinamica()
        tk.Label(self.area_dinamica, text="IMPRESIÓN DE DATOS", font=("Arial", 12)).pack(pady=10)

        texto = "Trabajadores registrados:\n\n"
        for trabajador in self.datos_trabajadores:
            num = trabajador["numero_trabajador"]
            turno = next((t["turno"] for t in self.turnos if t["numero_trabajador"] == num), "No asignado")
            horario = self.horarios_guardados.get(num, "No asignado")
            faltas = self.faltas_registradas.get(num, 0)
            periodo = self.periodos_vacacionales.get(num, "No asignado")

            texto += (f"Nombre: {trabajador['nombre']}\n"
                      f"Edad: {trabajador['edad']}\n"
                      f"Número de trabajador: {num}\n"
                      f"Género: {trabajador['genero']}\n"
                      f"Puesto: {trabajador['puesto']}\n"
                      f"Teléfono: {trabajador['telefono']}\n"
                      f"Correo: {trabajador['correo']}\n"
                      f"Turno: {turno}\n"
                      f"Horario: {horario}\n"
                      f"Faltas: {faltas}\n"
                      f"Periodo vacacional: {periodo}\n\n")

        text_area = tk.Text(self.area_dinamica, width=80, height=30)
        text_area.pack()
        text_area.insert("1.0", texto)
        text_area.config(state="disabled")


def ventana_principal():
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()


def ventana_inicio():
    inicio = tk.Tk()
    inicio.title("ACCESO A LA VENTANA")
    inicio.geometry("900x800")
    inicio.config(bg="khaki")

    tk.Label(inicio, text="CARGANDO....", font=("Arial", 39), bg="khaki").pack(pady=15)

    def abrir_app():
        inicio.destroy()
        ventana_principal()

    def salir():
        inicio.destroy()

    btn_entrada = tk.Button(inicio, text="Entrada al sistema", font=12, width=30, command=abrir_app, bg="linen")
    btn_entrada.pack(pady=5)

    btn_salida = tk.Button(inicio, text="Salida del sistema", font=12, width=30, command=salir, bg="linen")
    btn_salida.pack(pady=5)

    inicio.mainloop()

ventana_inicio()

