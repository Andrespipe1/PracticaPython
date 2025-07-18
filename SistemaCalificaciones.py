"""
Sistema de Gestión de Calificaciones
====================================

Este módulo implementa un sistema completo de gestión de calificaciones
que permite a los docentes registrar, ordenar y buscar calificaciones
de estudiantes utilizando diversos algoritmos.

Integrantes:
- Adria Ramos
- Andres Tufiño  
- Christian Marquez
- Richard Robalino
- Sebastian Chico

Fecha: 2024
"""

import os
import time
from typing import List, Tuple, Optional

# Configuración global
CREDENCIALES_DOCENTES = {
    "docente@esfot.edu.ec": "Docente2023*"
}

# Estructuras de datos globales
datos_profesores = [[], [], []]  # [nombres, apellidos, materias]
datos_alumnos = [[], [], []]     # [nombres, apellidos, calificaciones]


def limpiar_pantalla():
    """Limpia la pantalla del terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')


def validar_nota(nota: str) -> float:
    """
    Valida que la nota ingresada esté en el rango correcto (0-20).
    
    Args:
        nota: String con la nota a validar
        
    Returns:
        float: La nota validada
        
    Raises:
        ValueError: Si la nota no es válida
    """
    try:
        nota_float = float(nota)
        if 0 <= nota_float <= 20:
            return nota_float
        else:
            raise ValueError("La nota debe estar entre 0 y 20")
    except ValueError as e:
        if "La nota debe estar entre" in str(e):
            raise e
        else:
            raise ValueError("Por favor ingrese un número válido")


def login() -> bool:
    """
    Sistema de autenticación para docentes.
    
    Returns:
        bool: True si el login es exitoso, False en caso contrario
    """
    print("=" * 50)
    print("    Sistema de Gestión de Calificaciones")
    print("=" * 50)
    
    while True:
        usuario = input("Usuario: ").strip()
        contraseña = input("Contraseña: ").strip()
        
        if usuario in CREDENCIALES_DOCENTES and CREDENCIALES_DOCENTES[usuario] == contraseña:
            print("✅ Inicio de sesión exitoso.")
            time.sleep(1.5)
            return True
        else:
            print("❌ Credenciales incorrectas. Inténtelo de nuevo.")
            time.sleep(1.5)
            limpiar_pantalla()


def mostrar_menu_principal() -> int:
    """
    Muestra el menú principal y obtiene la opción del usuario.
    
    Returns:
        int: Opción seleccionada por el usuario
    """
    print("\n" + "=" * 40)
    print("           MENÚ PRINCIPAL")
    print("=" * 40)
    print("1. Registrar Datos (Profesor y Alumnos)")
    print("2. Ordenar Calificaciones")
    print("3. Buscar Calificaciones")
    print("4. Salir")
    print("=" * 40)
    
    while True:
        try:
            opcion = int(input("Seleccione una opción (1-4): "))
            if 1 <= opcion <= 4:
                return opcion
            else:
                print("❌ Por favor ingrese una opción válida (1-4)")
        except ValueError:
            print("❌ Por favor ingrese un número válido")


def ingresar_datos_profesor():
    """Registra los datos del profesor en el sistema."""
    print("\n" + "=" * 40)
    print("      REGISTRO DE DATOS DEL PROFESOR")
    print("=" * 40)
    
    nombre = input("Nombre: ").strip()
    while not nombre:
        print("❌ El nombre no puede estar vacío")
        nombre = input("Nombre: ").strip()
    
    apellido = input("Apellido: ").strip()
    while not apellido:
        print("❌ El apellido no puede estar vacío")
        apellido = input("Apellido: ").strip()
    
    materia = input("Materia: ").strip()
    while not materia:
        print("❌ La materia no puede estar vacía")
        materia = input("Materia: ").strip()
    
    # Almacenar datos
    datos_profesores[0].append(nombre)
    datos_profesores[1].append(apellido)
    datos_profesores[2].append(materia)
    
    print(f"✅ Profesor {nombre} {apellido} registrado exitosamente")


def ingresar_datos_alumnos(cantidad: int):
    """
    Registra los datos de múltiples alumnos.
    
    Args:
        cantidad: Número de alumnos a registrar
    """
    print(f"\n" + "=" * 40)
    print(f"      REGISTRO DE {cantidad} ALUMNOS")
    print("=" * 40)
    
    for i in range(cantidad):
        print(f"\n--- Alumno {i+1}/{cantidad} ---")
        
        nombre = input("Nombre: ").strip()
        while not nombre:
            print("❌ El nombre no puede estar vacío")
            nombre = input("Nombre: ").strip()
        
        apellido = input("Apellido: ").strip()
        while not apellido:
            print("❌ El apellido no puede estar vacío")
            apellido = input("Apellido: ").strip()
        
        while True:
            try:
                nota = validar_nota(input("Nota (0-20): "))
                break
            except ValueError as e:
                print(f"❌ {e}")
        
        # Almacenar datos
        datos_alumnos[0].append(nombre)
        datos_alumnos[1].append(apellido)
        datos_alumnos[2].append(nota)
        
        print(f"✅ Alumno {nombre} {apellido} registrado con nota {nota}")


def clasificar_calificacion(nota: float) -> str:
    """
    Clasifica una calificación según el sistema de puntuación.
    
    Args:
        nota: Calificación a clasificar
        
    Returns:
        str: Clasificación de la nota
    """
    if 0 <= nota <= 8:
        return "Reprobado"
    elif 9 <= nota <= 13:
        return "Suspenso"
    elif 14 <= nota <= 20:
        return "Aprobado"
    else:
        return "Nota fuera de rango"


def generar_reporte_calificaciones():
    """Genera un reporte completo de calificaciones en archivo de texto."""
    if not datos_alumnos[0]:
        print("❌ No hay datos de alumnos para generar el reporte")
        return
    
    aprobados = []
    suspendidos = []
    reprobados = []
    
    # Clasificar estudiantes
    for i, nota in enumerate(datos_alumnos[2]):
        clasificacion = clasificar_calificacion(nota)
        nombre_completo = f"{datos_alumnos[0][i]} {datos_alumnos[1][i]}"
        
        if clasificacion == "Aprobado":
            aprobados.append(nombre_completo)
        elif clasificacion == "Suspenso":
            suspendidos.append(nombre_completo)
        elif clasificacion == "Reprobado":
            reprobados.append(nombre_completo)
    
    # Calcular estadísticas
    suma_notas = sum(datos_alumnos[2])
    promedio_notas = suma_notas / len(datos_alumnos[2])
    
    # Generar archivo
    with open("calificaciones.txt", "w", encoding="utf-8") as archivo:
        archivo.write("\t\tESCUELA POLITÉCNICA NACIONAL\n\n")
        archivo.write("=" * 50 + "\n")
        archivo.write("              REPORTE DE CALIFICACIONES\n")
        archivo.write("=" * 50 + "\n\n")
        
        # Datos del profesor
        for i in range(len(datos_profesores[0])):
            archivo.write("DATOS DEL PROFESOR:\n")
            archivo.write("-" * 30 + "\n")
            archivo.write(f"Nombre: {datos_profesores[0][i]} {datos_profesores[1][i]}\n")
            archivo.write(f"Materia: {datos_profesores[2][i]}\n")
            archivo.write("-" * 30 + "\n\n")
        
        # Calificaciones de estudiantes
        archivo.write("CALIFICACIONES DE ESTUDIANTES:\n")
        archivo.write("-" * 40 + "\n")
        for i in range(len(datos_alumnos[0])):
            nombre = datos_alumnos[0][i]
            apellido = datos_alumnos[1][i]
            nota = datos_alumnos[2][i]
            clasificacion = clasificar_calificacion(nota)
            archivo.write(f"{nombre} {apellido}: {nota} - {clasificacion}\n")
        
        archivo.write("-" * 40 + "\n\n")
        
        # Estadísticas
        archivo.write("ESTADÍSTICAS:\n")
        archivo.write("-" * 20 + "\n")
        archivo.write(f"Promedio de notas: {promedio_notas:.2f}\n")
        archivo.write(f"Total de estudiantes: {len(datos_alumnos[0])}\n")
        archivo.write(f"Aprobados: {len(aprobados)}\n")
        archivo.write(f"Suspendidos: {len(suspendidos)}\n")
        archivo.write(f"Reprobados: {len(reprobados)}\n")
        archivo.write("-" * 20 + "\n\n")
        
        # Listas detalladas
        if aprobados:
            archivo.write("ESTUDIANTES APROBADOS:\n")
            archivo.write("-" * 25 + "\n")
            archivo.write(", ".join(aprobados) + "\n\n")
        
        if suspendidos:
            archivo.write("ESTUDIANTES SUSPENDIDOS:\n")
            archivo.write("-" * 25 + "\n")
            archivo.write(", ".join(suspendidos) + "\n\n")
        
        if reprobados:
            archivo.write("ESTUDIANTES REPROBADOS:\n")
            archivo.write("-" * 25 + "\n")
            archivo.write(", ".join(reprobados) + "\n\n")
    
    print("💾 Guardando datos...")
    time.sleep(1)
    print("✅ Archivo 'calificaciones.txt' generado exitosamente")


# Algoritmos de ordenamiento
def ordenamiento_burbuja(calificaciones: List[float], nombres: List[str]) -> Tuple[List[float], List[str]]:
    """
    Implementa el algoritmo de ordenamiento burbuja.
    
    Args:
        calificaciones: Lista de calificaciones
        nombres: Lista de nombres correspondientes
        
    Returns:
        Tuple con las listas ordenadas
    """
    calificaciones = calificaciones.copy()
    nombres = nombres.copy()
    n = len(calificaciones)
    
    for i in range(n-1):
        for j in range(n-1-i):
            if calificaciones[j] > calificaciones[j+1]:
                calificaciones[j], calificaciones[j+1] = calificaciones[j+1], calificaciones[j]
                nombres[j], nombres[j+1] = nombres[j+1], nombres[j]
    
    return calificaciones, nombres


def ordenamiento_seleccion(calificaciones: List[float], nombres: List[str]) -> Tuple[List[float], List[str]]:
    """
    Implementa el algoritmo de ordenamiento por selección.
    
    Args:
        calificaciones: Lista de calificaciones
        nombres: Lista de nombres correspondientes
        
    Returns:
        Tuple con las listas ordenadas
    """
    calificaciones = calificaciones.copy()
    nombres = nombres.copy()
    n = len(calificaciones)
    
    for i in range(n-1):
        menor = i
        for j in range(i+1, n):
            if calificaciones[j] < calificaciones[menor]:
                menor = j
        calificaciones[i], calificaciones[menor] = calificaciones[menor], calificaciones[i]
        nombres[i], nombres[menor] = nombres[menor], nombres[i]
    
    return calificaciones, nombres


def ordenamiento_insercion(calificaciones: List[float], nombres: List[str]) -> Tuple[List[float], List[str]]:
    """
    Implementa el algoritmo de ordenamiento por inserción.
    
    Args:
        calificaciones: Lista de calificaciones
        nombres: Lista de nombres correspondientes
        
    Returns:
        Tuple con las listas ordenadas
    """
    calificaciones = calificaciones.copy()
    nombres = nombres.copy()
    n = len(calificaciones)
    
    for i in range(1, n):
        actual_cal = calificaciones[i]
        actual_nom = nombres[i]
        j = i
        while j > 0 and calificaciones[j-1] > actual_cal:
            calificaciones[j] = calificaciones[j-1]
            nombres[j] = nombres[j-1]
            j -= 1
        calificaciones[j] = actual_cal
        nombres[j] = actual_nom
    
    return calificaciones, nombres


def ordenamiento_quicksort(calificaciones: List[float], nombres: List[str]) -> Tuple[List[float], List[str]]:
    """
    Implementa el algoritmo de ordenamiento QuickSort.
    
    Args:
        calificaciones: Lista de calificaciones
        nombres: Lista de nombres correspondientes
        
    Returns:
        Tuple con las listas ordenadas
    """
    if len(calificaciones) <= 1:
        return calificaciones, nombres
    
    pivot_cal = calificaciones[0]
    pivot_nom = nombres[0]
    
    menores_cal = [cal for cal in calificaciones[1:] if cal <= pivot_cal]
    menores_nom = [nombres[i+1] for i, cal in enumerate(calificaciones[1:]) if cal <= pivot_cal]
    
    mayores_cal = [cal for cal in calificaciones[1:] if cal > pivot_cal]
    mayores_nom = [nombres[i+1] for i, cal in enumerate(calificaciones[1:]) if cal > pivot_cal]
    
    menores_cal, menores_nom = ordenamiento_quicksort(menores_cal, menores_nom)
    mayores_cal, mayores_nom = ordenamiento_quicksort(mayores_cal, mayores_nom)
    
    return menores_cal + [pivot_cal] + mayores_cal, menores_nom + [pivot_nom] + mayores_nom


def merge(left_cal: List[float], left_nom: List[str], 
          right_cal: List[float], right_nom: List[str]) -> Tuple[List[float], List[str]]:
    """
    Función auxiliar para el algoritmo MergeSort.
    
    Args:
        left_cal: Calificaciones del lado izquierdo
        left_nom: Nombres del lado izquierdo
        right_cal: Calificaciones del lado derecho
        right_nom: Nombres del lado derecho
        
    Returns:
        Tuple con las listas fusionadas y ordenadas
    """
    result_cal = []
    result_nom = []
    i = j = 0
    
    while i < len(left_cal) and j < len(right_cal):
        if left_cal[i] <= right_cal[j]:
            result_cal.append(left_cal[i])
            result_nom.append(left_nom[i])
            i += 1
        else:
            result_cal.append(right_cal[j])
            result_nom.append(right_nom[j])
            j += 1
    
    result_cal.extend(left_cal[i:])
    result_nom.extend(left_nom[i:])
    result_cal.extend(right_cal[j:])
    result_nom.extend(right_nom[j:])
    
    return result_cal, result_nom


def ordenamiento_mergesort(calificaciones: List[float], nombres: List[str]) -> Tuple[List[float], List[str]]:
    """
    Implementa el algoritmo de ordenamiento MergeSort.
    
    Args:
        calificaciones: Lista de calificaciones
        nombres: Lista de nombres correspondientes
        
    Returns:
        Tuple con las listas ordenadas
    """
    if len(calificaciones) <= 1:
        return calificaciones, nombres
    
    mid = len(calificaciones) // 2
    left_cal = calificaciones[:mid]
    left_nom = nombres[:mid]
    right_cal = calificaciones[mid:]
    right_nom = nombres[mid:]
    
    left_cal, left_nom = ordenamiento_mergesort(left_cal, left_nom)
    right_cal, right_nom = ordenamiento_mergesort(right_cal, right_nom)
    
    return merge(left_cal, left_nom, right_cal, right_nom)


def mostrar_menu_ordenamiento() -> int:
    """
    Muestra el menú de algoritmos de ordenamiento.
    
    Returns:
        int: Opción seleccionada
    """
    print("\n" + "=" * 40)
    print("      ALGORITMOS DE ORDENAMIENTO")
    print("=" * 40)
    print("1. Burbuja (Bubble Sort)")
    print("2. Selección (Selection Sort)")
    print("3. Inserción (Insertion Sort)")
    print("4. Merge Sort")
    print("5. Quick Sort")
    print("6. Volver al menú principal")
    print("=" * 40)
    
    while True:
        try:
            opcion = int(input("Seleccione un algoritmo (1-6): "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("❌ Por favor ingrese una opción válida (1-6)")
        except ValueError:
            print("❌ Por favor ingrese un número válido")


def ordenar_calificaciones():
    """Función principal para ordenar calificaciones."""
    if not datos_alumnos[0]:
        print("❌ No hay datos de alumnos para ordenar")
        return
    
    opcion = mostrar_menu_ordenamiento()
    
    if opcion == 6:
        return
    
    # Seleccionar algoritmo
    algoritmos = {
        1: ("Burbuja", ordenamiento_burbuja),
        2: ("Selección", ordenamiento_seleccion),
        3: ("Inserción", ordenamiento_insercion),
        4: ("Merge Sort", ordenamiento_mergesort),
        5: ("Quick Sort", ordenamiento_quicksort)
    }
    
    nombre_algoritmo, funcion_algoritmo = algoritmos[opcion]
    
    print(f"\n🔄 Ordenando con algoritmo: {nombre_algoritmo}")
    calificaciones_ordenadas, nombres_ordenados = funcion_algoritmo(
        datos_alumnos[2], datos_alumnos[0]
    )
    
    # Mostrar resultados
    print(f"\n📊 Resultados ordenados ({nombre_algoritmo}):")
    print("-" * 40)
    for i, (nombre, calificacion) in enumerate(zip(nombres_ordenados, calificaciones_ordenadas)):
        print(f"{i+1:2d}. {nombre}: {calificacion}")
    
    # Generar archivo
    with open("ordenamiento.txt", "w", encoding="utf-8") as archivo:
        archivo.write("\t\tESCUELA POLITÉCNICA NACIONAL\n\n")
        archivo.write("=" * 50 + "\n")
        archivo.write("        CALIFICACIONES ORDENADAS\n")
        archivo.write("=" * 50 + "\n\n")
        archivo.write(f"Algoritmo utilizado: {nombre_algoritmo}\n")
        archivo.write("-" * 40 + "\n")
        for i, (nombre, calificacion) in enumerate(zip(nombres_ordenados, calificaciones_ordenadas)):
            archivo.write(f"{i+1:2d}. {nombre}: {calificacion}\n")
        archivo.write("-" * 40 + "\n")
    
    print(f"\n💾 Archivo 'ordenamiento.txt' generado exitosamente")


# Algoritmos de búsqueda
def busqueda_lineal(lista: List[float], valor: float) -> Optional[int]:
    """
    Implementa búsqueda lineal.
    
    Args:
        lista: Lista donde buscar
        valor: Valor a buscar
        
    Returns:
        int: Índice del valor encontrado, None si no se encuentra
    """
    for i, elemento in enumerate(lista):
        if elemento == valor:
            return i
    return None


def busqueda_binaria(lista: List[float], valor: float) -> Optional[int]:
    """
    Implementa búsqueda binaria (requiere lista ordenada).
    
    Args:
        lista: Lista ordenada donde buscar
        valor: Valor a buscar
        
    Returns:
        int: Índice del valor encontrado, None si no se encuentra
    """
    izquierda, derecha = 0, len(lista) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == valor:
            return medio
        elif lista[medio] < valor:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    
    return None


def busqueda_interpolacion(lista: List[float], valor: float) -> Optional[int]:
    """
    Implementa búsqueda por interpolación (requiere lista ordenada).
    
    Args:
        lista: Lista ordenada donde buscar
        valor: Valor a buscar
        
    Returns:
        int: Índice del valor encontrado, None si no se encuentra
    """
    izquierda, derecha = 0, len(lista) - 1
    
    while (izquierda <= derecha and 
           valor >= lista[izquierda] and 
           valor <= lista[derecha]):
        
        if izquierda == derecha:
            if lista[izquierda] == valor:
                return izquierda
            return None
        
        pos = izquierda + int(((valor - lista[izquierda]) * 
                              (derecha - izquierda)) / 
                              (lista[derecha] - lista[izquierda]))
        
        if lista[pos] == valor:
            return pos
        elif lista[pos] < valor:
            izquierda = pos + 1
        else:
            derecha = pos - 1
    
    return None


def mostrar_menu_busqueda() -> int:
    """
    Muestra el menú de algoritmos de búsqueda.
    
    Returns:
        int: Opción seleccionada
    """
    print("\n" + "=" * 40)
    print("      ALGORITMOS DE BÚSQUEDA")
    print("=" * 40)
    print("1. Búsqueda Lineal")
    print("2. Búsqueda Binaria")
    print("3. Búsqueda por Interpolación")
    print("4. Volver al menú principal")
    print("=" * 40)
    
    while True:
        try:
            opcion = int(input("Seleccione un algoritmo (1-4): "))
            if 1 <= opcion <= 4:
                return opcion
            else:
                print("❌ Por favor ingrese una opción válida (1-4)")
        except ValueError:
            print("❌ Por favor ingrese un número válido")


def buscar_calificacion():
    """Función principal para buscar calificaciones."""
    if not datos_alumnos[0]:
        print("❌ No hay datos de alumnos para buscar")
        return
    
    # Obtener calificación a buscar
    while True:
        try:
            calificacion = validar_nota(input("Ingrese la calificación a buscar (0-20): "))
            break
        except ValueError as e:
            print(f"❌ {e}")
    
    opcion = mostrar_menu_busqueda()
    
    if opcion == 4:
        return
    
    # Seleccionar algoritmo
    algoritmos = {
        1: ("Búsqueda Lineal", busqueda_lineal),
        2: ("Búsqueda Binaria", busqueda_binaria),
        3: ("Búsqueda por Interpolación", busqueda_interpolacion)
    }
    
    nombre_algoritmo, funcion_busqueda = algoritmos[opcion]
    
    # Para búsqueda binaria e interpolación, necesitamos lista ordenada
    if opcion in [2, 3]:
        calificaciones_ordenadas = sorted(datos_alumnos[2])
        resultado = funcion_busqueda(calificaciones_ordenadas, calificacion)
    else:
        resultado = funcion_busqueda(datos_alumnos[2], calificacion)
    
    # Mostrar resultados
    print(f"\n🔍 Buscando calificación {calificacion} con {nombre_algoritmo}")
    
    if resultado is not None:
        if opcion in [2, 3]:
            # Para algoritmos que usan lista ordenada, buscar en lista original
            indices_originales = [i for i, cal in enumerate(datos_alumnos[2]) if cal == calificacion]
            if indices_originales:
                for idx in indices_originales:
                    nombre = datos_alumnos[0][idx]
                    apellido = datos_alumnos[1][idx]
                    print(f"✅ Encontrado: {nombre} {apellido} - {calificacion}")
        else:
            nombre = datos_alumnos[0][resultado]
            apellido = datos_alumnos[1][resultado]
            print(f"✅ Encontrado: {nombre} {apellido} - {calificacion}")
    else:
        print("❌ Calificación no encontrada")
    
    # Generar archivo de búsqueda
    with open("búsqueda.txt", "w", encoding="utf-8") as archivo:
        archivo.write("\t\tESCUELA POLITÉCNICA NACIONAL\n\n")
        archivo.write("=" * 50 + "\n")
        archivo.write("           BÚSQUEDA DE CALIFICACIONES\n")
        archivo.write("=" * 50 + "\n\n")
        archivo.write(f"Algoritmo utilizado: {nombre_algoritmo}\n")
        archivo.write(f"Calificación buscada: {calificacion}\n")
        archivo.write("-" * 40 + "\n")
        
        if resultado is not None:
            if opcion in [2, 3]:
                indices_originales = [i for i, cal in enumerate(datos_alumnos[2]) if cal == calificacion]
                for idx in indices_originales:
                    nombre = datos_alumnos[0][idx]
                    apellido = datos_alumnos[1][idx]
                    archivo.write(f"✅ {nombre} {apellido}: {calificacion}\n")
            else:
                nombre = datos_alumnos[0][resultado]
                apellido = datos_alumnos[1][resultado]
                archivo.write(f"✅ {nombre} {apellido}: {calificacion}\n")
        else:
            archivo.write("❌ Calificación no encontrada\n")
        
        archivo.write("-" * 40 + "\n")
    
    print(f"\n💾 Archivo 'búsqueda.txt' generado exitosamente")


def main():
    """Función principal del programa."""
    # Autenticación
    if not login():
        print("❌ No se pudo autenticar. Saliendo del programa.")
        return
    
    limpiar_pantalla()
    print("🎓 ¡Bienvenido al Sistema de Gestión de Calificaciones!")
    
    while True:
        opcion = mostrar_menu_principal()
        
        if opcion == 1:
            limpiar_pantalla()
            ingresar_datos_profesor()
            
            while True:
                try:
                    cantidad = int(input("\nIngrese la cantidad de alumnos: "))
                    if cantidad > 0:
                        break
                    else:
                        print("❌ La cantidad debe ser mayor a 0")
                except ValueError:
                    print("❌ Por favor ingrese un número válido")
            
            ingresar_datos_alumnos(cantidad)
            generar_reporte_calificaciones()
            
        elif opcion == 2:
            limpiar_pantalla()
            ordenar_calificaciones()
            
        elif opcion == 3:
            limpiar_pantalla()
            buscar_calificacion()
            
        elif opcion == 4:
            print("\n👋 ¡Gracias por usar nuestro sistema!")
            print("Desarrollado con ❤️ por estudiantes de la EPN")
            break
        
        input("\nPresione Enter para continuar...")
        limpiar_pantalla()


if __name__ == "__main__":
    main()