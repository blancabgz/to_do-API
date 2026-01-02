from app.models import Task

class InMemoryTaskRepository:
    def __init__(self):
        self.tasks = {}
        self.next_id = 1

    def add(self, title:str) -> Task:
        task = Task(id=self.next_id,
                    title=title,
                    completed=False
                )
        self.tasks[self.next_id] = task
        self.next_id += 1
        return task
    

        