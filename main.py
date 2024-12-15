import sys
import os

# Añadir el directorio raíz del proyecto al path de Python
project_root = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, project_root)

# Modificar la importación
from src.app import main as streamlit_app

if __name__ == "__main__":
    streamlit_app()