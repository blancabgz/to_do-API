from app.repository import InMemoryTaskRepository
from app.models import Task


def create_task(repo: InMemoryTaskRepository, title: str) -> Task:
    if title is not None and not isinstance(title, str):
        raise TypeError("Title must be a string")
    if not title or title.strip() == "":
        raise ValueError("Title cannot be empty")
    if len(title) > 255:
        raise ValueError("Title cannot exceed 255 characters")
    
    return repo.add(title)
