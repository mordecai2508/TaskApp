import streamlit as st
from .database import get_db, engine
from .models import Base
from .crud import (
    create_task, 
    get_tasks, 
    update_task_status, 
    delete_completed_tasks,
    export_tasks_to_json,
    import_tasks_from_json
)
from datetime import datetime

# Crear todas las tablas en la base de datos
Base.metadata.create_all(bind=engine)

def main():
    st.title("🚀 Task Management Pro")

    # Obtener sesión de base de datos
    db = next(get_db())

    # Menú de navegación
    menu = ["Agregar Tarea", "Listar Tareas", "Exportar/Importar"]
    choice = st.sidebar.selectbox("Menú", menu)

    if choice == "Agregar Tarea":
        st.subheader("Crear Nueva Tarea")
        
        # Formulario de nueva tarea
        col1, col2 = st.columns(2)
        
        with col1:
            title = st.text_input("Título de la Tarea *")
        
        with col2:
            due_date = st.date_input("Fecha de Vencimiento", min_value=datetime.now())
        
        description = st.text_area("Descripción (Opcional)")
        
        if st.button("Guardar Tarea"):
            if title:
                try:
                    create_task(
                        db, 
                        title=title, 
                        description=description, 
                        due_date=due_date
                    )
                    st.success("Tarea agregada exitosamente")
                except Exception as e:
                    st.error(f"Error al guardar la tarea: {e}")
            else:
                st.warning("El título es obligatorio")

    elif choice == "Listar Tareas":
        st.subheader("📋 Mis Tareas")
        
        # Filtros de tareas
        filter_option = st.selectbox(
            "Filtrar Tareas", 
            ["Todas", "Pendientes", "Completadas"]
        )

        # Obtener tareas según el filtro
        if filter_option == "Todas":
            tasks = get_tasks(db)
        elif filter_option == "Pendientes":
            tasks = get_tasks(db, completed=False)
        else:
            tasks = get_tasks(db, completed=True)

        # Mostrar tareas
        for task in tasks:
            with st.expander(f"🔹 {task.title}"):
                st.write(f"**Descripción:** {task.description or 'Sin descripción'}")
                st.write(f"**Fecha de creación:** {task.created_at}")
                st.write(f"**Fecha de vencimiento:** {task.due_date or 'Sin fecha'}")
                
                col1, col2 = st.columns(2)
                with col1:
                    if not task.completed:
                        if st.button(f"Completar Tarea {task.id}", key=f"complete_{task.id}"):
                            update_task_status(db, task.id, True)
                            st.experimental_rerun()
                with col2:
                    st.checkbox("Completada", value=task.completed, disabled=True)

        # Botón para eliminar tareas completadas
        if st.button("🗑️ Eliminar Tareas Completadas"):
            deleted_count = delete_completed_tasks(db)
            st.success(f"Se eliminaron {deleted_count} tareas completadas")
            st.experimental_rerun()

    elif choice == "Exportar/Importar":
        st.subheader("📤 Exportar / 📥 Importar Tareas")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Exportar Tareas")
            export_file = st.text_input("Nombre de archivo para exportar", value="tasks_export.json")
            if st.button("Exportar a JSON"):
                try:
                    export_tasks_to_json(db, export_file)
                    st.success(f"Tareas exportadas a {export_file}")
                except Exception as e:
                    st.error(f"Error al exportar: {e}")
        
        with col2:
            st.subheader("Importar Tareas")
            import_file = st.text_input("Ruta del archivo JSON")
            if st.button("Importar desde JSON"):
                try:
                    import_tasks_from_json(db, import_file)
                    st.success("Tareas importadas exitosamente")
                    st.experimental_rerun()
                except Exception as e:
                    st.error(f"Error al importar: {e}")

if __name__ == "__main__":
    main()