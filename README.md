# Proyecto PFO2 - Sistema de Gestión de Tareas

Este proyecto consiste en una API desarrollada con Flask y una interfaz cliente en consola para gestionar usuarios y tareas. La base de datos utilizada es SQLite.

## Requisitos

- Python 3.10 o superior  
- `pip` (instalador de paquetes de Python)  
- Sistema operativo Windows, Linux o macOS  

## Instalación

1. Clonar el repositorio o descargar los archivos del proyecto.

2. Crear un entorno virtual (opcional pero recomendado):

  ```bash
   python -m venv venv
   source venv/bin/activate     # en Linux/macOS
   .\venv\Scripts\activate      # en Windows
  ```
3. Instalar dependencias
  ```bash
  pip install -r requirements.txt
  ```
## Ejecutar el Servidor y verificar la base de datos
Desde la raíz del proyecto:

1. Ejecutar el servidor una vez para que cree automáticamente el archivo tareas_pfo2.db
  ```bash
  py servidor.py
  ```
2. Verificar que se haya creado la base en instance/tareas_pfo2.db.

Por defecto, el servidor se ejecutará en: http://127.0.0.1:5000/

## Ejecutar el cliente en consola

Desde la carpeta donde está el archivo cliente.py, ejecutar:
  ```bash
  py cliente.py
  ```
Esto mostrará un menú interactivo para registrarse, iniciar sesión y ver tareas.

## Comandos útiles de SQLite
Para inspeccionar la base de datos:

1. Abrir la terminal y navegar a la carpeta instance/.

2. Ejecutar:
  ```bash
  sqlite3 tareas_pfo2.db
  ```
Comandos dentro de SQLite:
  ```bash
    .tables
    .schema usuario
    SELECT * FROM usuario;
    .exit
  ```


