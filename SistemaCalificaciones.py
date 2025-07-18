#INTEGRANTES: ADRIA RAMOS | ANDRES TUFIÑO | CHRISTIAN MARQUEZ | RICHARD ROBALINO | SEBASTIAN CHICO 

from os import system
import time

datosProfesores=[[],[],[]]
datosAlumnos = [[], [], []]

credenciales_docentes = {
    "docente@esfot.edu.ec": "Docente2023*"
}

def login():

    print("=== Sistema de Gestión de Calificaciones ===")
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    
    if usuario in credenciales_docentes and credenciales_docentes[usuario] == contraseña:
        print("Inicio de sesión exitoso.")
        time.sleep(2)
        return True
    else:
        print("Credenciales incorrectas. Inténtelo de nuevo.")
        time.sleep(2)
        return False

def menuOpciones():
  print("¿Que accion desea realizar?")
  print("1) Registrar Datos profesor y alumnos")
  print("2) Ordenar Calificaciones")
  print("3) Buscar Calificaciones")
  print("4) Salir")
  return int(input("Ingrese la opcion: "))


def ingresarDatosProfe():
  print("Ingrese los datos del Profesor: ")
  nombreProfe=input("- Nombre: ")
  apellidoProfe=input("- Apellido: ")
  materiaProfe=input("- Materia: ")
  datosProfesores[0].append(nombreProfe)
  datosProfesores[1].append(apellidoProfe)
  datosProfesores[2].append(materiaProfe)


def ingresarDatosAlumno(cantidadAlumnos):
  for i in range(cantidadAlumnos):
    print(f"Ingrese los datos del Alumno {i+1}: ")
    nombreAlumno = input("- Nombre: ")
    apellidoAlumno = input("- Apellido: ")
    notaAlumno = float(input("- Nota: "))
    datosAlumnos[0].append(nombreAlumno)
    datosAlumnos[1].append(apellidoAlumno)
    datosAlumnos[2].append(notaAlumno)


def calificacion_texto(nota):
    if 0 <= nota <= 8:
        return "Reprobado"
    elif 9 <= nota <= 13:
        return "Suspenso"
    elif 14 <= nota <= 20:
        return "Aprobado"
    else:
        return "Nota fuera de rango"

def archivarTXT():
  aprobados = []
  suspendidos = []
  reprobados = []
  with open("calificaciones.txt", "a", encoding="utf-8") as archivo:
    suma_notas = sum(datosAlumnos[2])
    promedio_notas = suma_notas / len(datosAlumnos[2])
    for i in range(len(datosProfesores[0])):
      archivo.write("\tESCUELA POLITECNICA NACIONAL\n\n")
      archivo.write("Reporte de notas\n")
      archivo.write("----------------------------------\n")
      archivo.write(f"* Datos Profesor {i+1}\n")
      archivo.write(f"* {datosProfesores[0][i]} {datosProfesores[1][i]}\n")
      archivo.write(f"* Materia: {datosProfesores[2][i]}\n")
      archivo.write("----------------------------------\n")
    for i in range(len(datosAlumnos[0])):
      archivo.write(f"*   {datosAlumnos[0][i]} {datosAlumnos[1][i]}\tNota: {datosAlumnos[2][i]} - {calificacion_texto(datosAlumnos[2][i])}\n")
        
    for nota, nombre in zip(datosAlumnos[2], datosAlumnos[0]):
      calif_texto = calificacion_texto(nota)
      if calif_texto == "Aprobado":
        aprobados.append(nombre)
      elif calif_texto == "Suspenso":
        suspendidos.append(nombre)
      elif calif_texto == "Reprobado":
        reprobados.append(nombre)
    archivo.write("----------------------------------\n")
    archivo.write(f"* Promedio de notas: {promedio_notas:.2f}\n")
    archivo.write("----------------------------------\n")
    archivo.write("* Estudiantes Aprobados:\n")
    archivo.write(", ".join(aprobados) + "\n")
    archivo.write("----------------------------------\n")
    archivo.write("* Estudiantes Suspendidos:\n")
    archivo.write(", ".join(suspendidos) + "\n")
    archivo.write("----------------------------------\n")
    archivo.write("* Estudiantes Reprobados:\n")
    archivo.write(", ".join(reprobados) + "\n")
    archivo.write("----------------------------------\n\n")

  print("Guardando datos....")
  time.sleep(1)
  print("\n---- Archivo generado exitosamente ------\n")
 
  
def ord_burbuja(arreglo_calificaciones, arreglo_nombres):
  n = len(arreglo_calificaciones)
  for i in range(n-1):
    for j in range(n-1-i): 
      if arreglo_calificaciones[j] > arreglo_calificaciones[j+1]:
        arreglo_calificaciones[j], arreglo_calificaciones[j+1] = arreglo_calificaciones[j+1], arreglo_calificaciones[j]
        arreglo_nombres[j], arreglo_nombres[j+1] = arreglo_nombres[j+1], arreglo_nombres[j]
  return arreglo_calificaciones, arreglo_nombres


def ord_seleccion(arreglo_calificaciones, arreglo_nombres):
    n = len(arreglo_calificaciones)
    for i in range(n-1):
        menor = i
        for j in range(i+1, n):
            if arreglo_calificaciones[j] < arreglo_calificaciones[menor]:
                menor = j
        arreglo_calificaciones[i], arreglo_calificaciones[menor] = arreglo_calificaciones[menor], arreglo_calificaciones[i]
        arreglo_nombres[i], arreglo_nombres[menor] = arreglo_nombres[menor], arreglo_nombres[i]
    return arreglo_calificaciones, arreglo_nombres


def ord_insercion(arreglo_calificaciones, arreglo_nombres):
    n = len(arreglo_calificaciones)
    for i in range(1, n):
        actual = arreglo_calificaciones[i]
        actual_nombre = arreglo_nombres[i]
        j = i
        while j > 0 and arreglo_calificaciones[j - 1] > actual:
            arreglo_calificaciones[j] = arreglo_calificaciones[j - 1]
            arreglo_nombres[j] = arreglo_nombres[j - 1]
            j -= 1
        arreglo_calificaciones[j] = actual
        arreglo_nombres[j] = actual_nombre
    return arreglo_calificaciones, arreglo_nombres


def ord_quicksort(arreglo_calificaciones, arreglo_nombres):
    if len(arreglo_calificaciones) <= 1:
        return arreglo_calificaciones, arreglo_nombres
    else:
        pivot = arreglo_calificaciones[0]
        left_calificaciones = [x for x in arreglo_calificaciones[1:] if x <= pivot]
        left_nombres = [arreglo_nombres[i+1] for i, x in enumerate(arreglo_calificaciones[1:]) if x <= pivot]
        right_calificaciones = [x for x in arreglo_calificaciones[1:] if x > pivot]
        right_nombres = [arreglo_nombres[i+1] for i, x in enumerate(arreglo_calificaciones[1:]) if x > pivot]
        left_calificaciones, left_nombres = ord_quicksort(left_calificaciones, left_nombres)
        right_calificaciones, right_nombres = ord_quicksort(right_calificaciones, right_nombres)
        return left_calificaciones + [pivot] + right_calificaciones, left_nombres + [arreglo_nombres[0]] + right_nombres
 

def ord_merge(left_calificaciones, left_nombres, right_calificaciones, right_nombres):
    result_calificaciones = []
    result_nombres = []
    i = j = 0
    while i < len(left_calificaciones) and j < len(right_calificaciones):
        if left_calificaciones[i] < right_calificaciones[j]:
            result_calificaciones.append(left_calificaciones[i])
            result_nombres.append(left_nombres[i])
            i += 1
        else:
            result_calificaciones.append(right_calificaciones[j])
            result_nombres.append(right_nombres[j])
            j += 1
    result_calificaciones.extend(left_calificaciones[i:])
    result_nombres.extend(left_nombres[i:])
    result_calificaciones.extend(right_calificaciones[j:])
    result_nombres.extend(right_nombres[j:])
    return result_calificaciones, result_nombres

def ord_mergesort(arreglo_calificaciones, arreglo_nombres):
    if len(arreglo_calificaciones) <= 1:
        return arreglo_calificaciones, arreglo_nombres
    else:
        mid = len(arreglo_calificaciones) // 2
        left_calificaciones = arreglo_calificaciones[:mid]
        left_nombres = arreglo_nombres[:mid]
        right_calificaciones = arreglo_calificaciones[mid:]
        right_nombres = arreglo_nombres[mid:]

        left_calificaciones, left_nombres = ord_mergesort(left_calificaciones, left_nombres)
        right_calificaciones, right_nombres = ord_mergesort(right_calificaciones, right_nombres)

        return ord_merge(left_calificaciones, left_nombres, right_calificaciones, right_nombres)


def ordTXT(calificaciones, nombres, tipo_ordenamiento):
    with open("ordenamiento.txt", "w", encoding="utf-8") as archivo:
        archivo.write("\t\tESCUELA POLITECNICA NACIONAL\n\n")
        archivo.write("-------------Calificaciones Ordenadas-------------\n")
        archivo.write(f"Tipo de ordenamiento: {tipo_ordenamiento}\n")
        for calificacion, nombre in zip(calificaciones, nombres):
            archivo.write(f'{nombre}: {calificacion}\n')
        archivo.write("--------------------------------------------------\n\n")    
    print("Guardando datos....")
    time.sleep(1)
    print("\n---- Archivo generado exitosamente ------\n")


def ordenarCalificaciones(listaCalificaciones, listaNombres):
    print("Por qué método quiere ordenar las calificaciones?")
    print("1) Burbuja")
    print("2) Seleccion")
    print("3) Insercion")
    print("4) Mergesort")
    print("5) Quicksort")
    print("6) Salir")
    opcion = int(input("Ingrese la opcion: "))
    tipo_ordenamiento = ""
    if opcion == 1:
        tipo_ordenamiento = "Burbuja"
        listaCalificaciones, listaNombres = ord_burbuja(listaCalificaciones, listaNombres)
    elif opcion == 2:
        tipo_ordenamiento = "Seleccion"
        listaCalificaciones, listaNombres = ord_seleccion(listaCalificaciones, listaNombres)
    elif opcion == 3:
        tipo_ordenamiento = "Insercion"
        listaCalificaciones, listaNombres = ord_insercion(listaCalificaciones, listaNombres)
    elif opcion == 4:
        tipo_ordenamiento = "Mergesort"
        listaCalificaciones, listaNombres = ord_mergesort(listaCalificaciones, listaNombres)
    elif opcion == 5:
        tipo_ordenamiento = "Quicksort"
        listaCalificaciones, listaNombres = ord_quicksort(listaCalificaciones, listaNombres)
    elif opcion == 6:
        print("Saliendo del programa")
    else:
        print("Opcion invalida")

    if opcion in [1, 2, 3, 4, 5]:
        ordTXT(listaCalificaciones, listaNombres, tipo_ordenamiento)


def busqueda_lineal(lista, valor):
  for i in range(len(lista)):
    if lista[i] == valor:
      return i
  return -1


def busqueda_binaria(lista, valor):
  izquierda, derecha = 0, len(lista) - 1
  while izquierda <= derecha:
      medio = (izquierda + derecha) // 2
      if lista[medio] == valor:
          return medio
      elif lista[medio] < valor:
          izquierda = medio + 1
      else:
          derecha = medio - 1
  return -1


def busqueda_interpolacion(lista, valor):
  izquierda, derecha = 0, len(lista) - 1
  while izquierda <= derecha and valor >= lista[izquierda] and valor <= lista[derecha]:
      pos = izquierda + ((valor - lista[izquierda]) * (derecha - izquierda)) // (lista[derecha] - lista[izquierda])
      if lista[pos] == valor:
          return pos
      if lista[pos] < valor:
          izquierda = pos + 1
      else:
          derecha = pos - 1
  return -1


def buscarCalificacion():
  calificacion = float(input("Ingrese la calificación a buscar: "))
  algoritmo = input("Seleccione el algoritmo de búsqueda\n\t1) lineal\n\t2) binaria\n\t3) interpolación)\n")

  if algoritmo.lower() == "1":
      busqueda_lineal(datosAlumnos[2], calificacion)
      busquedaTXT(calificacion,algoritmo)
  elif algoritmo.lower() == "2":
      busqueda_binaria(datosAlumnos[2], calificacion)
      busquedaTXT(calificacion,algoritmo)
  elif algoritmo.lower() == "3":
      busqueda_interpolacion(datosAlumnos[2], calificacion)
      busquedaTXT(calificacion,algoritmo)
  else:
      print("Algoritmo no reconocido")
      return


def busquedaTXT(calificacion,algoritmo):
  archivo = open("búsqueda.txt", "a", encoding="utf-8")
  archivo.write("---------------------------\n")
  archivo.write("\tCOLEGIO o UNIVERSIDAD Epn\n\n")
  archivo.write("Búsqueda de Calificaciones\n")
  archivo.write(f"ALGORITMO: {algoritmo}\n")
  archivo.write(f"\tLa calificación a buscar fue de: {calificacion }\n")
  
  if calificacion in datosAlumnos[2]:
    index = datosAlumnos[2].index(calificacion)
    archivo.write(f"\n\tCorresponde al estudiante: {datosAlumnos[0][index]} {datosAlumnos[1][index]}\n")
    archivo.write(f"\tNombre de profesor: {datosProfesores[0][0]} {datosProfesores[1][0]}\n")
    archivo.write("--------------------------------------------\n")
    print(f"\tLa calificación a buscar fue de: {calificacion }")
    print(f"\tCorresponde al estudiante: {datosAlumnos[0][index]} {datosAlumnos[1][index]}")
    print(f"\tNombre de profesor: {datosProfesores[0][0]} {datosProfesores[1][0]}")
  else:
    archivo.write("La calificación no se encontró en los datos.\n")
    print("La calificación no se encontró en los datos.\n")

  archivo.close()
  print("Resultados almacenados en el archivo búsqueda.txt\n")


def main():
  while not login():
        pass 
  system("cls")
  print("---- Bienvenido al sistema de notas -----")
  opcion = menuOpciones()
  while opcion != 4:
    if opcion == 1:
      system("cls")
      ingresarDatosProfe()
      cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))
      ingresarDatosAlumno(cantidad_alumnos)
      archivarTXT()
      opcion = menuOpciones()
    if opcion == 2:
      system("cls")
      ordenarCalificaciones(datosAlumnos[2], datosAlumnos[0])
      opcion = menuOpciones()
    if opcion == 3:
      system("cls")
      buscarCalificacion()
      opcion=menuOpciones()
    if opcion == 4:
      print("¡Gracias por usar nuestro sistema!")
      exit()
    else:
      print("Opción no valida")
      opcion=menuOpciones()

main()