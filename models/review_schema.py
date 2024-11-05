from pydantic import BaseModel

class ReviewBase(BaseModel):
    game_id: int
    user_id: int
    review_text: str
    rating: int

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int

    class Config:
        orm_mode = True
