from sqlalchemy.orm import Session
from .models import Task
from typing import List, Optional
from datetime import datetime

def create_task(db: Session, title: str, description: Optional[str] = None, 
                due_date: Optional[datetime] = None) -> Task:
    """
    Crear una nueva tarea
    """
    db_task = Task(
        title=title, 
        description=description, 
        due_date=due_date
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks(db: Session, completed: Optional[bool] = None) -> List[Task]:
    """
    Obtener tareas, con opción de filtrar por estado
    """
    query = db.query(Task)
    if completed is not None:
        query = query.filter(Task.completed == completed)
    return query.all()

def update_task_status(db: Session, task_id: int, completed: bool) -> Optional[Task]:
    """
    Actualizar el estado de una tarea
    """
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        task.completed = completed
        db.commit()
        db.refresh(task)
    return task

def delete_completed_tasks(db: Session) -> int:
    """
    Eliminar todas las tareas completadas
    """
    deleted_count = db.query(Task).filter(Task.completed == True).delete()
    db.commit()
    return deleted_count

def export_tasks_to_json(db: Session, file_path: str):
    """
    Exportar tareas a un archivo JSON
    """
    import json
    tasks = get_tasks(db)
    tasks_data = [
        {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "completed": task.completed,
            "created_at": task.created_at.isoformat() if task.created_at else None,
            "due_date": task.due_date.isoformat() if task.due_date else None
        } for task in tasks
    ]
    
    with open(file_path, 'w') as f:
        json.dump(tasks_data, f, indent=4)

def import_tasks_from_json(db: Session, file_path: str):
    """
    Importar tareas desde un archivo JSON
    """
    import json
    from datetime import datetime

    with open(file_path, 'r') as f:
        tasks_data = json.load(f)
    
    for task_data in tasks_data:
        # Convertir fechas de cadena a objetos datetime
        created_at = datetime.fromisoformat(task_data['created_at']) if task_data['created_at'] else None
        due_date = datetime.fromisoformat(task_data['due_date']) if task_data['due_date'] else None
        
        # Crear nueva tarea
        db_task = Task(
            title=task_data['title'],
            description=task_data.get('description'),
            completed=task_data['completed'],
            created_at=created_at,
            due_date=due_date
        )
        db.add(db_task)
    
    db.commit()