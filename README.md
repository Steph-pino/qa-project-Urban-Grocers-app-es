# Project-Urban-Grocers-app-es

Descripción del Proyecto:
Este proyecto hace parte del Bootcamp QA y tiene como objetivo realizar pruebas de la API de la aplicación *Urban Grocers*, específicamente en la creación de un kit para usuarios en la plataforma. 

# Archivos y directorios:
- configuration.py: Configuración para las rutas y credenciales necesarias para interactuar con la API.
- data.py: Datos que se utilizan en las pruebas.
- sender_stand_request.py: Archivo que maneja las solicitudes para la creación de usuarios y kits.
- create_kit_name_kit_test.py: Contiene la lista de comprobación para las pruebas.
- .gitignore: Archivos y carpetas que no deben ser seguidos por Git.

# Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal del proyecto.
- **pytest**: Framework de pruebas utilizado para automatizar y gestionar las pruebas.
- **Requests**: Biblioteca de Python para realizar solicitudes HTTP.

# Instalación y Uso:

1. Clonar el repositorio:
Abre la terminal y navega al directorio donde quieres almacenar tus proyectos.

cd ~
mkdir projects
cd projects
git clone git@github.com:username/qa-project-Urban-Grocers-app-es.git

2. Crear y activar un entorno virtual:
python -m venv venv
source venv/bin/activate   # En Linux/macOS
.\venv\Scripts\activate    # En Windows

3. Instalar las dependencias:
pip install -r requirements.txt

4. Abrir el proyecto en PyCharm:
Abre PyCharm y selecciona Archivo → Abrir, luego selecciona la carpeta qa-project-Urban-Grocers-app-es.

5. Iniciar el servidor:
Una vez el servidor se inicie, abre el navegador y accede a la URL de la API: <url-del-servidor>/docs/

# Procedimiento para Crear un Kit:

1. Crear un usuario: Envía una solicitud para crear un nuevo usuario y obtener el **authToken**.
2. Crear un kit: Con el **authToken** obtenido, envía una solicitud para crear un kit para ese usuario. 

# Ejecutar las Pruebas:

Para ejecutar las pruebas con PyTest, usa el siguiente comando en la terminal:

pytest qa-project-Urban-Grocers-app-es

# Contribuciones

Si deseas contribuir, por favor sigue los pasos:

1. Realiza un fork del proyecto.
2. Crea una rama con tus cambios: `git checkout -b mi-rama`.
3. Envía un pull request describiendo tus modificaciones.

---

**Autor**: Stephanie Pino para el Sprint 7
