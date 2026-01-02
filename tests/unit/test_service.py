import pytest

from app.repository import InMemoryTaskRepository
from app.service import create_task

# TEST: Crear una tarea correctamente
def test_create_task():
    repo = InMemoryTaskRepository()
    task = create_task(repo, title="Hacer la práctica DS")

    # Verificar que la tarea se creó correctamente
    assert task.id == 1 
    assert task.title == "Hacer la práctica DS"
    assert task.completed is False

# TEST: No crear una tarea con título vacío
def test_create_task_empty_title():
    repo = InMemoryTaskRepository()
    
    with pytest.raises(ValueError) as excinfo:
        create_task(repo, title="")
    
    assert "Title cannot be empty" in str(excinfo.value)

# TEST: Verificar que los IDs se incrementan correctamente
def test_create_task_increment_id():
    repo = InMemoryTaskRepository()
    task1 = create_task(repo, title="Tarea 1")
    task2 = create_task(repo, title="Tarea 2")

    assert task1.id == 1
    assert task2.id == 2

# TEST: No crear una tarea con título demasiado largo
def test_create_task_long_title():
    repo = InMemoryTaskRepository()
    long_title = "A" * 300 

    with pytest.raises(ValueError) as excinfo:
        create_task(repo, title=long_title)
    
    assert "Title cannot exceed 255 characters" in str(excinfo.value)

# TEST: No crear una tarea con título no string
def test_create_task_non_string_title():
    repo = InMemoryTaskRepository()
    
    with pytest.raises(TypeError) as excinfo:
        create_task(repo, title=12345)  
    
    assert "Title must be a string" in str(excinfo.value)