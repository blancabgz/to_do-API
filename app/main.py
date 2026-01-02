from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
from app.repository import InMemoryTaskRepository
from app.service import create_task

app = FastAPI(title="TO-DO API", version="0.1.0")
repo = InMemoryTaskRepository()

class TaskCreate(BaseModel):
    title: str
    
class TaskResponse(BaseModel):
    id: int
    title: str
    completed: bool

@app.get("/health")
def health():
    return{"status" : "ok"}

@app.post("/tasks", response_model=TaskResponse, status_code=201)
def create_task_endpoint(request: TaskCreate):
    try:
        task = create_task(repo, title=request.title)
        return TaskResponse(id=task.id, title=task.title, completed=task.completed)
    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

