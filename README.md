# Sistema de Gestión de Calificaciones

## 📚 Descripción

Sistema de gestión de calificaciones desarrollado en Python que permite a los docentes registrar, ordenar y buscar calificaciones de estudiantes. El sistema incluye múltiples algoritmos de ordenamiento y búsqueda, además de generar reportes en formato de texto.

- **Andres Tufiño**

## 🚀 Características Principales

### 🔐 Sistema de Autenticación

- Login seguro para docentes
- Credenciales predefinidas para acceso al sistema

### 📊 Gestión de Datos

- Registro de datos de profesores (nombre, apellido, materia)
- Registro de datos de estudiantes (nombre, apellido, calificación)
- Validación de calificaciones (0-20 puntos)

### 📈 Algoritmos de Ordenamiento

El sistema implementa 5 algoritmos de ordenamiento diferentes:

1. **Burbuja (Bubble Sort)** - O(n²)
2. **Selección (Selection Sort)** - O(n²)
3. **Inserción (Insertion Sort)** - O(n²)
4. **Merge Sort** - O(n log n)
5. **Quick Sort** - O(n log n)

### 🔍 Algoritmos de Búsqueda

Implementa 3 algoritmos de búsqueda:

1. **Búsqueda Lineal** - O(n)
2. **Búsqueda Binaria** - O(log n)
3. **Búsqueda por Interpolación** - O(log log n)

### 📄 Generación de Reportes

- **calificaciones.txt**: Reporte completo con estadísticas
- **ordenamiento.txt**: Resultados de ordenamiento
- **búsqueda.txt**: Resultados de búsquedas

## 🛠️ Instalación y Uso

### Requisitos

- Python 3.6 o superior
- Sistema operativo: Windows, macOS, Linux

### Ejecución

```bash
python SistemaCalificaciones.py
```

### Credenciales de Acceso

- **Usuario**: docente@esfot.edu.ec
- **Contraseña**: Docente2023\*

## 📋 Funcionalidades

### 1. Registro de Datos

- Ingreso de información del profesor
- Registro de múltiples estudiantes
- Validación automática de calificaciones

### 2. Ordenamiento de Calificaciones

- Selección del algoritmo de ordenamiento
- Visualización de resultados ordenados
- Generación de archivo con resultados

### 3. Búsqueda de Calificaciones

- Búsqueda por calificación específica
- Selección del algoritmo de búsqueda
- Visualización de resultados

### 4. Generación de Reportes

- Estadísticas de aprobación
- Promedio de calificaciones
- Clasificación de estudiantes por rendimiento

## 📊 Clasificación de Calificaciones

- **0-8 puntos**: Reprobado
- **9-13 puntos**: Suspenso
- **14-20 puntos**: Aprobado

## 📁 Estructura de Archivos

```
PracticaPython/
├── SistemaCalificaciones.py    # Código principal
├── README.md                   # Documentación
├── calificaciones.txt          # Reporte de calificaciones (generado)
├── ordenamiento.txt            # Resultados de ordenamiento (generado)
└── búsqueda.txt               # Resultados de búsqueda (generado)
```

## 🔧 Tecnologías Utilizadas

- **Lenguaje**: Python 3
- **Estructuras de Datos**: Listas, Diccionarios
- **Algoritmos**: Ordenamiento y Búsqueda
- **Manejo de Archivos**: Escritura y lectura de archivos de texto

## 📝 Notas de Desarrollo

- El sistema está diseñado para ser intuitivo y fácil de usar
- Todos los algoritmos están implementados desde cero
- Los reportes se generan en formato UTF-8 para compatibilidad
- El código incluye comentarios explicativos para facilitar el mantenimiento

## 🤝 Contribuciones

Este proyecto fue desarrollado como práctica académica.

---
