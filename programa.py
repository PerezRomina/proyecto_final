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

    self.menu_lateral= tk.Frame(self.root,bg="light salmon",width=10)
    self.menu_lateral.pack(side="right",expand=True,fill="both")
    self.crear_menu
    self.saludo

  
  def crear_menu(self):
    tk.Button(self.menu_lateral,text="INICIO",command=self.saludo,widht=18).pack(pady=10)
    tk.Button(self.menu_lateral, text="REGISTRO",command= self.registro, widht=18).pack(pady=10)
    tk.Button(self.menu_lateral, text="PUESTOS", command=self.puestos, widht=18).pack(pady=10)
    tk.Button(self.menu_lateral, text="ASISTENCIAS", command=self.asistecias, widht=18).pack(pady=10)
    tk.Button(selfmenu_lateral, text="PERIODO VACACIONAL", command=self.periodo, widht=18).pack(pady=10)

  
  def limpiar_area_dinamica(self):
     for widget in self.area_dinamica.winfo_childre():
         widget.destroy()
       
  def saludo(self):
     self.limpiar_area_dinamica()
     tk.Label(self.area_dinamica, text="Aquí va el mensaje de bienvenida", font("Arial",14)).pack(pady=10)
     tk.Button(self.area_dinamica, text="Mosatrar mensaje de bienvenida")
          command=lambda:messagebox.showinfo("Bienvenido", "Hola bienvenida")).pack()
    
  def trabajador(self)
     self.limpiar_area_dinamica()
     tk.Label(self.area_dinamica, text="Registro de los datos del trabajador", font=("Arial", 12)).pack(pady=10)
     tk.Label(self.area_dinamica, text="Nombre:").pack()
     nombre = tk.Entry(self.area_dinamica)
     nombre.pack(pady=5)

   
  
    

  
  print("CONTROL DE AISTENCIAS DE TRABAJADOR")
  print("--Registre los datos del trabajador")
  nombre=input("Inrese el nombre del trabajador \n")
  control=input("Ingrese el numero de control \n")
  edad=input("Ingresa la edad del trabajador \n")
  genero=input("Ingresa el genero del trabajador \n")

  print("\n ---Puestos---")
  print("1)Doctor")
  print("2)Pediatra")
  print("3)Enfermer@")
  print("4)Recepcion")
  
  puestos=input("Selecciona el puesto del trabajador(1-4): ")
  if puestos=="1":
      print("El trbajador tiene el puesto de Doctor")
  elif puestos=="2":
      print("El trabajador tiene el puesto en pediatría ")
  elif puestos=="3":
      print("El trabajador tiene puesto en enfermería")
  elif puestos=="4":
      print("El trabador tiene puesto en recepcion recepcion")
  else:
    print("ERROR,NO SE ENCUENTRA OTRO PUESTO")

  print("\n ----CONTROL DE ASISTENCIAS----")
  print("Asitencias de dias por semana")
  print("1)Un dia,esta semana")
  print("2)Dos dias,esta semana")
  print("3)Tres dias,esta semana")
  print("4)Cuatro dias,esta semana")
  print("5)Asisstió la semana completa")

  asistencias = input("¿Cuántos días a la semana asistió el trabajador? (1-5): ")

  if asistencias == '1':
        print("El trabajador solo asistió UN día.")
  elif asistencias == '2':
        print("El trabajador solo asistió DOS días.")
  elif asistencias == '3':
        print("El trabajador solo asistió TRES días.")
  elif asistencias == '4':
        print("El trabajador solo asistió CUATRO días.")
  elif asistencias == '5':
        print("El trabajador asistió la semana completa.")
  else:
        print("Opción inválida.")
  print("\n ---PERIODO VACACIONAL---")
  print("¿Cual es el periodo vacacional seleccionado para el trabajador?")
  print("1)Enero-Febrero")
  print("2)Febrero-Marzo")
  print("3)Marzo-Abril")
  print("4)Abril-Mayo")
  print("5)Mayo-Junio")
  print("6)Junio-Julio")
  print("7)Julio-Agosto")
  print("8)Agosto-Septiembre")
  print("9)Septiembre-Octumbre")
  print("10)Octubre-Noviembre")
  print("11)Noviembre-Diciembre")

  periodo=input("Seleccione el periodo vacacional")
  if periodo=="1":
    print("El trabajador tiene permitido el perido vacacional ENERO-FEBRERO")
  elif periodo=="2":
    print("El trabajador tiene permitido el periodo vacacional FEBRERO-MARZO")
  elif periodo=="3":
     print("El trabajador tiene permitido el periodo vacacional MARZO-ABRIL")
  elif periodo=="4":
     print("El trabajador tiene permitido el periodo vacacional ABRIL-MAYO")
  elif periodo=="5":
     print("El trabajador tiene permitido el periodo vacacional MAYO-JUNIO")
  elif periodo=="6":
     print("El trabajador tiene permitido el periodo vacacional JUNIO-JULIO")
  elif periodo=="7":
    print("El trabajador tiene permitido el periodo vacacional JULIO-AGOSTO")
  elif periodo=="8":
     print("El trabajador tiene permitido el periodo vacacional AGOSTO-SEPTIEMBRE")
  elif periodo=="9":
     print("El trabajador tiene permitido el periodo vacacional SEPTIEMBRE-OCTUBRE")
  elif periodo=="10":
     print("El trabajador tiene permitido el periodo vacacional OCTUBRE-NOVIMEMBRE")
  elif periodo=="11":
     print("El trabajador tiene el periodo vacacional NOVIEMBRE.DICIEMBRE")
  else:
     print("Periodo NO valido")

control_asistencia_trabajador()

