from repositories.user_repository import UserRepository
from models.user_model import User as UserModel
from models.user_schema import UserCreate

class UserService:
    def __init__(self):
        self.repository = UserRepository()

    def create_user(self, user: UserCreate):
        user_model = UserModel(**user.dict())  
        return self.repository.create(user_model)

    def authenticate_user(self, username: str, password: str):
        return self.repository.authenticate(username, password)

    def get_favorites(self, user_id: int):
        return self.repository.get_favorites(user_id)

    def add_favorite(self, user_id: int, game_id: int):
        return self.repository.add_favorite(user_id, game_id)

    def remove_favorite(self, user_id: int, game_id: int):
        return self.repository.remove_favorite(user_id, game_id)