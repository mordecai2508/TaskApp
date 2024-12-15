# 📋 Task Management Pro

## 🚀 Descripción del Proyecto

Task Management Pro es una aplicación robusta de gestión de tareas desarrollada en Python, diseñada para ayudar a los usuarios a organizar, rastrear y administrar sus tareas diarias de manera eficiente.

## ✨ Características Principales

- 🆕 Creación de tareas con título, descripción y fecha de vencimiento
- 📝 Listado completo de tareas
- ✅ Marcado de tareas como completadas
- 🗑️ Eliminación de tareas completadas
- 📤 Exportación de tareas a formato JSON
- 📥 Importación de tareas desde archivo JSON

## 🛠️ Tecnologías Utilizadas

- **Lenguaje**: Python 3.8+
- **Framework de Interfaz**: Streamlit
- **ORM**: SQLAlchemy
- **Base de Datos**: SQLite
- **Gestión de Dependencias**: pip

## 📦 Requisitos Previos

- Python 3.8 o superior
- pip (Gestor de paquetes de Python)
- Entorno virtual (recomendado)

## 🔧 Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/mordecai2508/TaskApp.git)
```

2. Crear y activar un entorno virtual:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## 🚀 Ejecución de la Aplicación

```bash
streamlit run main.py
```

## 📂 Estructura del Proyecto

```
TaskApp/
│
├── src/                  
│   ├── __init__.py       
│   ├── database.py       
│   ├── models.py         
│   ├── crud.py           
│   └── app.py            
│
├── config.py             
├── main.py               
└── requirements.txt      
```

## 📋 Uso de la Aplicación

1. **Agregar Tarea**:
   - Ingresa un título (obligatorio)
   - Añade una descripción (opcional)
   - Selecciona una fecha de vencimiento
     ![image](https://github.com/user-attachments/assets/9ac7d8ae-c796-4b92-a94b-2381dc97419c)



2. **Gestionar Tareas**:
   - Marca tareas como completadas
   - Elimina tareas completadas
   - Filtra tareas por estado

   ![image](https://github.com/user-attachments/assets/369f69d9-7d74-4052-adb3-9fdef0e73ece)

   ![image](https://github.com/user-attachments/assets/a6d6db97-0107-40b7-bd30-f926c3318ccb)



4. **Exportar/Importar**:
   - Exporta tareas a un archivo JSON
   - Importa tareas desde un archivo JSON existente

![image](https://github.com/user-attachments/assets/0ce5a937-2b39-4a6e-9215-472ad91ce9bf)


## 📞 Contacto

Carlos Daniel Ramirez Avendaño 

Enlace del Proyecto: [(https://github.com/mordecai2508/TaskApp.git)]

## 🙏 Agradecimientos

- [Streamlit](https://streamlit.io/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Python](https://www.python.org/)
