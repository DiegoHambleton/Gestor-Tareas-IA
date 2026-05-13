import json
from pathlib import Path
from tasks.models import Task

DATA_FILE = Path.home() / ".task-cli-data.json"

def load_tasks() -> list[Task]:
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE) as f:
        return [Task.from_dict(t) for t in json.load(f)]

def save_tasks(tasks: list[Task]) -> None:
    with open(DATA_FILE, "w") as f:
        json.dump([t.to_dict() for t in tasks], f, indent=2, ensure_ascii=False)

def add_task(task: Task) -> None:
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)

def get_task_by_id(task_id: str) -> Task | None:
    return next((t for t in load_tasks() if t.id == task_id), None)

def update_task(updated: Task) -> None:
    tasks = [updated if t.id == updated.id else t for t in load_tasks()]
    save_tasks(tasks)

def delete_task(task_id: str) -> None:
    save_tasks([t for t in load_tasks() if t.id != task_id])