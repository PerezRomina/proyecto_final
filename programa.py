import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("CONTROL ASISTENCIAS HOSPITAL")
        self.root.config(bg="lightblue")
        self.root.geometry("700x600")

        self.datos_trabajadores = []   
        self.turnos = []               
        self.faltas_registradas = {}  
        self.periodos_vacacionales = {}

        self.menu_lateral = tk.Frame(self.root, bg="light salmon", width=150)
        self.menu_lateral.pack(side="left", fill="y")

        self.area_dinamica = tk.Frame(self.root, bg="bisque")
        self.area_dinamica.pack(side="right", expand=True, fill="both")

        self.crear_menu()
        self.saludo()

    def crear_menu(self):
        tk.Button(self.menu_lateral, text="📌INICIO", font="Times 14 bold", command=self.saludo, width=20).pack(pady=10)
        tk.Button(self.menu_lateral, text="📃REGISTRO", font="Times 14 bold", command=self.trabajador, width=20).pack(pady=10)
        tk.Button(self.menu_lateral, text="TURNO", font="Times 14 bold", command=self.turno, width=20).pack(pady=10)
        tk.Button(self.menu_lateral, text="🏢FALTAS", font="Times 14 bold", command=self.faltas, width=20).pack(pady=10)
        tk.Button(self.menu_lateral, text="PERIODO VACACIONAL", font="Times 14 bold", command=self.periodo_vacacional, width=20).pack(pady=10)
        tk.Button(self.menu_lateral, text="IMPRESIÓN DE DATOS", font="Times 14 bold", command=self.imprimir, width=20).pack(pady=10)

    def limpiar_area_dinamica(self):
        for widget in self.area_dinamica.winfo_children():
            widget.destroy()

    def saludo(self):
        self.limpiar_area_dinamica()
        tk.Label(self.area_dinamica, text="Bienvenido al sistema de asistencia", font=("Arial", 14)).pack(pady=10)
        tk.Button(self.area_dinamica, text="Mostrar mensaje de bienvenida",
                  command=lambda: messagebox.showinfo("Bienvenido", "Hola, bienvenido")).pack()

    def trabajador(self):
        self.limpiar_area_dinamica()
        tk.Label(self.area_dinamica, text="Registro de los datos del trabajador", font=("Arial", 12)).pack(pady=10)

        tk.Label(self.area_dinamica, text="Nombre:").pack()
        nombre_entry = tk.Entry(self.area_dinamica)
        nombre_entry.pack()

        tk.Label(self.area_dinamica, text="Edad:").pack()
        edad_entry = tk.Entry(self.area_dinamica)
        edad_entry.pack()

        tk.Label(self.area_dinamica, text="Número de trabajador:").pack()
        num_trab_entry = tk.Entry(self.area_dinamica)
        num_trab_entry.pack()

        tk.Label(self.area_dinamica, text="Género:").pack()
        genero_combo = ttk.Combobox(self.area_dinamica, values=["Masculino", "Femenino"])
        genero_combo.pack()

        tk.Label(self.area_dinamica, text="Puesto:").pack()
        puesto_combo = ttk.Combobox(self.area_dinamica, values=["Medico", "Pediatra", "Doctor", "Recepcionista"])
        puesto_combo.pack()

        def guardar_datos():
            numero = num_trab_entry.get()
            if not numero.isdigit():
                messagebox.showerror("Error", "El número de trabajador debe ser numérico.")
                return

            datos = {
                "nombre": nombre_entry.get(),
                "edad": edad_entry.get(),
                "numero_trabajador": numero,
                "genero": genero_combo.get(),
                "puesto": puesto_combo.get()
            }

            if not all(datos.values()):
                messagebox.showwarning("Campos incompletos", "Por favor completa todos los campos.")
                return

            for trabajador in self.datos_trabajadores:
                if trabajador["numero_trabajador"] == numero:
                    messagebox.showwarning("Duplicado", "Ya existe un trabajador con ese número.")
                    return

            self.datos_trabajadores.append(datos)
            messagebox.showinfo("Registro exitoso", "Datos guardados correctamente")

        tk.Button(self.area_dinamica, text="Guardar", command=guardar_datos).pack(pady=10)

    def turno(self):
        self.limpiar_area_dinamica()
        tk.Label(self.area_dinamica, text="TURNO DEL TRABAJADOR", font=("Arial", 12)).pack(pady=10)

        tk.Label(self.area_dinamica, text="Número de trabajador:").pack()
        num_trab_entry = tk.Entry(self.area_dinamica)
        num_trab_entry.pack()

        tk.Label(self.area_dinamica, text="Selecciona el turno:").pack()
        turno_combo = ttk.Combobox(self.area_dinamica, values=["Matutino", "Tarde", "Nocturno"])
        turno_combo.pack()

        def guardar_turno():
            numero = num_trab_entry.get()
            turno = turno_combo.get() 
            
            if not numero or not turno:
                messagebox.showwarning("Campos incompletos", "Completa todos los campos")
                return

            self.turnos = [t for t in self.turnos if t["numero_trabajador"] != numero]
            self.turnos.append({"numero_trabajador": numero, "turno": turno})

            messagebox.showinfo("Turno guardado", f"Turno '{turno}' asignado al trabajador {numero}")

        tk.Button(self.area_dinamica, text="Guardar turno", command=guardar_turno, bg="pink").pack(pady=15)

    def faltas(self):
        self.limpiar_area_dinamica()
        tk.Label(self.area_dinamica, text="REGISTRO DE FALTAS", font=("Arial", 12)).pack(pady=10)

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
                messagebox.showerror("Error", "Número de trabajador inválido.")
                return

            if numero not in [t["numero_trabajador"] for t in self.datos_trabajadores]:
                messagebox.showerror("No existe", "Este trabajador no está registrado.")
                return

            try:
                faltas_num = int(faltas_str.split()[0])
            except:
                messagebox.showerror("Error", "Selecciona una cantidad válida de faltas.")
                return

            self.faltas_registradas[numero] = self.faltas_registradas.get(numero, 0) + faltas_num
            messagebox.showinfo("Falta registrada", f"{faltas_num} falta(s) registrada(s) para el trabajador {numero}")

        tk.Button(self.area_dinamica, text="Registrar falta", command=registrar_falta).pack(pady=10)

    def periodo_vacacional(self):
        self.limpiar_area_dinamica()
        tk.Label(self.area_dinamica, text="PERIODO VACACIONAL", font=("Arial", 12)).pack(pady=10)

        tk.Label(self.area_dinamica, text="Número de trabajador:").pack()
        num_trab_entry = tk.Entry(self.area_dinamica)
        num_trab_entry.pack()

        tk.Label(self.area_dinamica, text="Selecciona el periodo vacacional:").pack()
        periodo_combo = ttk.Combobox(self.area_dinamica, values=[
            "Enero-Febrero", "Febrero-Marzo", "Marzo-Abril", "Abril-Mayo", "Mayo-Junio",
            "Junio-Julio", "Julio-Agosto", "Agosto-Septiembre", "Septiembre-Octubre", "Octubre-Noviembre", "Noviembre-Diciembre"
        ])
        periodo_combo.pack()

        def guardar_periodo():
            numero = num_trab_entry.get()
            periodo = periodo_combo.get()

            if not numero.isdigit():
                messagebox.showerror("Error", "Número de trabajador inválido.")
                return

            if numero not in [t["numero_trabajador"] for t in self.datos_trabajadores]:
                messagebox.showerror("No existe", "Este trabajador no está registrado.")
                return

            if not periodo:
                messagebox.showwarning("Campos incompletos", "Selecciona un periodo vacacional.")
                return

            self.periodos_vacacionales[numero] = periodo
            messagebox.showinfo("Periodo guardado", f"Periodo '{periodo}' registrado para el trabajador {numero}")

        tk.Button(self.area_dinamica, text="Guardar periodo", command=guardar_periodo).pack(pady=10)

    def imprimir(self):
        self.limpiar_area_dinamica()
        tk.Label(self.area_dinamica, text="LISTA DE TRABAJADORES", font=("Arial", 14)).pack(pady=10)

        if not self.datos_trabajadores:
            tk.Label(self.area_dinamica, text="Aún no hay datos").pack()
            return

        trabajadores_ordenados = sorted(self.datos_trabajadores, key=lambda x: x["numero_trabajador"])

        total_faltas = 0  
        for persona in trabajadores_ordenados:
            numero = persona["numero_trabajador"]
            turno = next((t["turno"] for t in self.turnos if t["numero_trabajador"] == numero), "Sin turno")
            faltas = self.faltas_registradas.get(numero, 0)
            periodo = self.periodos_vacacionales.get(numero, "No asignado")
            total_faltas += faltas  

            texto = (
                f"{persona['nombre']} | Edad: {persona['edad']} | N°: {numero} | Género: {persona['genero']} "
                f"| Puesto: {persona['puesto']} | Turno: {turno} | Faltas: {faltas} | Vacaciones: {periodo}"
            )
            tk.Label(self.area_dinamica, text=texto, bg="white").pack(anchor="w", padx=10, pady=3)

        tk.Label(self.area_dinamica, text=f"\nTOTAL GENERAL DE FALTAS: {total_faltas}", font=("Arial", 12, "bold"), fg="red").pack(pady=10)


if __name__ == "__main__":
    ventana = tk.Tk()
    app = Aplicacion(ventana)
    ventana.mainloop()

