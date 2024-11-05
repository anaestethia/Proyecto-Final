from sqlalchemy import Column, Integer, String, ForeignKey
from models.database import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    game_id = Column(Integer, ForeignKey("games.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    review_text = Column(String)
    rating = Column(Integer)