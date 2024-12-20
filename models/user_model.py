from sqlalchemy import Column, Integer, String
from models.database import Base
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    def verify_password(self, password: str):
        return pwd_context.verify(password, self.password)

    @classmethod
    def hash_password(cls, password: str):
        return pwd_context.hash(password)