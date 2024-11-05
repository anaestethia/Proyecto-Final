from models.database import SessionLocal
from models.user_model import User
from models.favorite_model import Favorite

class UserRepository:
    def __init__(self):
        self.db = SessionLocal()

    def create(self, user: User):
        user.password = User.hash_password(user.password)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def authenticate(self, username: str, password: str):
        user = self.db.query(User).filter(User.username == username).first()
        if user and user.verify_password(password):
            return user
        return None

    def get_favorites(self, user_id: int):
        return self.db.query(Favorite).filter(Favorite.user_id == user_id).all()

    def add_favorite(self, user_id: int, game_id: int):
        favorite = Favorite(user_id=user_id, game_id=game_id)
        self.db.add(favorite)
        self.db.commit()
        return favorite

    def remove_favorite(self, user_id: int, game_id: int):
        favorite = self.db.query(Favorite).filter(Favorite.user_id == user_id, Favorite.game_id == game_id).first()
        if favorite:
            self.db.delete(favorite)
            self.db.commit()
            return favorite
        return None