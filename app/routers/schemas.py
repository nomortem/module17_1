from pydantic import BaseModel
from typing import List, Optional

# Схема для пользователя
class UserBase(BaseModel):
    username: str
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    age: Optional[int] = None
    slug: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

# Схема для задачи
class TaskBase(BaseModel):
    title: str
    content: Optional[str] = None
    priority: int = 0
    completed: bool = False
    slug: str

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True