from dataclasses import dataclass, field
from datetime import datetime
import uuid

@dataclass
class Task:
    title: str
    description: str = ""
    priority: str = "media"   # baja | media | alta
    done: bool = False
    id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())

    def to_dict(self) -> dict:
        return self.__dict__

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        return cls(**data)