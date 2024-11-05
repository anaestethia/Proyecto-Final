from sqlalchemy import Column, Integer, String, Date
from models.database import Base

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    genre = Column(String)
    platform = Column(String)
    developer = Column(String)
    release_date = Column(Date)
    description = Column(String)