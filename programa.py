# main
def control_asistencia_trabajador():
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
  if puestos=="2":
      print("El trabajador tiene el puesto en pediatría ")
  if puestos=="3":
      print("El trabajador tiene puesto en enfermería")
  if puestos=="4":
      print("El trabador tiene puesto en recepcion recepcion")
    
control_asistencia_trabajador()
