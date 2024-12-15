import os

# Configuración de la base de datos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'tasks.db')}"

# Otras configuraciones del proyecto
PROJECT_NAME = "Task Management Pro"
VERSION = "1.0.0"