efi_ppy - Sistema de Gestión para Venta de Celulares
Descripción
efi_ppy es un sistema web desarrollado como parte de la Evaluación Final Integradora del curso. El objetivo del proyecto es gestionar equipos, modelos, fabricantes, características, y más, en un local de venta de celulares. El sistema permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre diversas entidades del negocio, asegurando una administración eficiente y organizada.

Características
Modelos principales: Incluye la gestión de equipos, modelos, fabricantes, características, stock, proveedores, accesorios, clientes, ventas y órdenes de pago.
Interfaz de usuario: Diseño sencillo y accesible, con navegación clara entre las diferentes secciones del sistema.
CRUD completo: Funcionalidades de creación, edición, visualización y eliminación para cada uno de los modelos definidos.
Templates reutilizables: Uso de un template base para evitar la repetición de código y mantener un diseño coherente en todo el sistema.
Tecnologías Utilizadas
Flask: Framework principal para la creación de la aplicación web.
Flask-SQLAlchemy: ORM para la gestión de la base de datos.
Flask-Migrate: Herramienta para el manejo de migraciones de la base de datos.
HTML/CSS: Para la estructura y estilo de las páginas web.
Jinja2: Motor de templates utilizado en Flask.
Instalación
Requisitos Previos
Python 3.10+
Virtualenv (opcional pero recomendado)
Instrucciones de Instalación:
1- Clona este repositorio: git clone https://github.com/tu_usuario/efi_ppy.git
cd efi_ppy

2- Crea un entorno virtual: python3 -m venv venv
source venv/bin/activate

3- Instala las dependencias necesarias: pip install -r requirements.txt

4- Configura la base de datos: flask db init
flask db migrate
flask db upgrade

5- Inicia la aplicación: flask run --reload 

6- Accede a la aplicación en tu navegador: http://127.0.0.1:5000

Uso
Navegación
Inicio: Resumen de las funcionalidades del sistema.
Gestión de Equipos: Permite ver, crear, editar y eliminar equipos.
Gestión de Modelos: Administra los modelos de los equipos.
Gestión de Fabricantes: Controla la información de los fabricantes.
Gestión de Características: Maneja las características técnicas de los equipos.
Gestión de Stock: Administra el stock disponible de cada equipo.
Gestión de Proveedores: Administra los datos de los proveedores.
Gestión de Accesorios: Controla los accesorios disponibles y su compatibilidad.
Gestión de Clientes: Administra la información de los clientes.
Gestión de Ventas: Registra y gestiona las ventas realizadas.
Gestión de Órdenes de Pago: Administra las órdenes de pago, incluyendo selección de clientes, productos, y formas de pago.
Funcionalidades CRUD
Para cada modelo, el sistema permite:

Crear: Añadir nuevos registros a la base de datos.
Leer: Visualizar los registros existentes.
Actualizar: Modificar los registros existentes.
Eliminar: Borrar registros de la base de datos.
Documentación Adicional:
Recursos Sugeridos
Documentación de Flask: https://flask-es.readthedocs.io/
Documentación de Flask-SQLAlchemy: https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/
Documentación de Flask-Migrate: https://flask-migrate.readthedocs.io/en/latest/


