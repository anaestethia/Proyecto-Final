from pydantic import BaseModel

class FavoriteBase(BaseModel):
    user_id: int
    game_id: int

class Favorite(FavoriteBase):
    class Config:
        orm_mode = True
