# main
import tkinter as tk
from tkinter import messagebox
from tkinter import tkk
class Aplicacion:
  def __init__(self,root):
    self.root= root
    self.root.title("CONTROL ASISTENCIAS HOSPITAL")
    self.root.geometry("600x700")
    self.root.config(bg="lightblue")

    self.datos_trabajadores[]
    
    self.menu_lateral= tk.Frame(self.root,bg="light salmon",width=10)
    self.menu_lateral.pack(side="left",fill="y")

    self.area_dinamica = tk.Frame(self.root, bg="bisque")
    self.area_dinamica.pack(side="right", expand=True, fill="both")
    self.crear_menu()
    self.saludo()

  
  def crear_menu(self):
    tk.Button(self.menu_lateral,text="INICIO",command=self.saludo,widht=18).pack(pady=10)
    tk.Button(self.menu_lateral, text="REGISTRO",command= self.registro, widht=18).pack(pady=10)
    tk.Button(self.menu_lateral, text="TURNO", command=self.turno, widht=18).pack(pady=10)
    tk.Button(self.menu_lateral, text="FALTAS", command=self.faltas, widht=18).pack(pady=10)
    tk.Button(selfmenu_lateral, text="IMPRESION", command=self.impresion, widht=18).pack(pady=10)

  
  def limpiar_area_dinamica(self):
     for widget in self.area_dinamica.winfo_childre():
         widget.destroy()
       
  def saludo(self):
     self.limpiar_area_dinamica()
     tk.Label(self.area_dinamica, text="CONTROL ASISTENCIAS", font("Arial",17)).pack(pady=10)
     tk.Button(self.area_dinamica, text="BIENVENIDA")
          command=lambda:messagebox.showinfo("Buen dia!", "Bienvenido al sistema de control de asistencias")).pack()

  
    
  def trabajador(self)
     self.limpiar_area_dinamica()
     tk.Label(self.area_dinamica, text="Registro de los datos del trabajador", font=("Arial", 12)).pack(pady=10)

     tk.Label(self.area_dinamica, text="Nombre:").pack()
     nombre_entry = tk.Entry(self.area_dinamica)
     nombre.pack(pady=5)
    
     tk.Label(self.area_dinamica, text="Número de trabajador:").pack()
     num_trab_entry = tk.Entry(self.area_dinamica)
     num_trab_entry.pack()

     tk.Label(self.area_dinamica, text="Seleccione su género:").pack()
     genero_combo = ttk.Combobox(self.area_dinamica, values=["Masculino", "Femenino"])
     genero_combo.pack()
  def guardar_datos():
     datos={
         "nombre": nombre_entry.get(),
         "edad": edad_entry.get(),
         "numero": num_trab_entry.get(),
         "genero": genero_combo.get()
     }
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
        tk.Button(self.area_dinamica, text="Guardar turno", command=guardar_turno, bg="pink").pack(pady=15)


    def faltas(self):
       self.limpiar_area_dinamica()
       tk.Label(self.area_dinamica, text=
        
  

             


  def imprimir(self):
      self.limpiar_area_dinamica()
      tk.Label(self.area_dinamica, text="LISTA DE TRABAJADORES", font=("Arial", 14)).pack(pady=10)

  if not self.datos_trabajadores:
     tk.Label(self.area_dinamica, text="Aún no hay datos").pack()
   return

   for persona in self.datos_trabajadores:
       turno = "Sin turno"
   for t in self.turnos:
   if t["numero_trabajador"] == persona["numero_trabajador"]:
       turno = t["turno"]
   break

    texto = f"{persona['nombre']} | Edad: {persona['edad']} | N°: {persona['numero_trabajador']} | Género: {persona['genero']} | Turno: {turno}"
    tk.Label(self.area_dinamica, text=texto, bg="white").pack(anchor="w", padx=10, pady=3)

if __name__ == "__main__":
    ventana = tk.Tk()
    app = Aplicacion(ventana)
    ventana.mainloop()

