from pydantic import BaseModel
from datetime import date

class GameBase(BaseModel):
    title: str
    genre: str
    platform: str
    developer: str
    release_date: date
    description: str

class GameCreate(GameBase):
    pass

class Game(GameBase):
    id: int

    class Config:
        orm_mode = True
