from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# TEST: Crear una tarea correctamente devuelve 201 y datos de la tarea
def test_create_task_return_201_and_task_data():
    response = client.post("/tasks/", json={"title": "Nueva tarea"})
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == "Nueva tarea"
    assert data["completed"] is False

# TEST: Crear una tarea con título vacío devuelve error 400
def test_create_task_empty_title_returns_400():
    response = client.post("/tasks/", json={"title": ""})
    assert response.status_code == 400
    data = response.json()
    assert "Title cannot be empty" in data["detail"]