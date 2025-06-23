Sistema de Adopción de Perros - Proyecto IFTS11

Este proyecto es un sistema web desarrollado para gestionar la adopción de perros. Fue creado como trabajo grupal para la materia Programación Orientada a Objetos (POO) en el IFTS11.

Tecnologías utilizadas

•	Django 5.2.3  
•	Python 3.13.5  
•	Base de datos: SQLite 

Instalación y uso

1. Clonar el repositorio

git clone https://github.com/Joa6jb/IFTS11-POO-2025-GRUPAL.git
cd IFTS11-POO-2025-GRUPAL

2. Crear y activar un entorno virtual 
•	En Windows:
  python -m venv venv
  venv\Scripts\activate

•	En macOS / Linux:
  python3 -m venv venv
  source venv/bin/activate

3. Instalar django
  pip install django

4. Aplicar migraciones
  python manage.py migrate

5. Crear superusuario
  python manage.py createsuperuser

Seguir las instrucciones en pantalla para crear un usuario administrador.

6. Ejecutar el servidor
  python manage.py runserver

7. Acceder desde el navegador

Ingresar a la siguiente URL:
http://127.0.0.1:8000/admin
