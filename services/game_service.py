from repositories.game_repository import GameRepository
from models.game_model import Game as GameModel
from models.game_schema import GameCreate

class GameService:
    def __init__(self):
        self.repository = GameRepository()

    def create_game(self, game: GameCreate):
        game_model = GameModel(**game.dict())
        return self.repository.create(game_model)

    def get_all_games(self):
        return self.repository.get_all()

    def get_game(self, game_id: int):
        return self.repository.get(game_id)

    def update_game(self, game_id: int, game: GameCreate):
        game_model = GameModel(**game.dict())
        return self.repository.update(game_id, game_model)

    def delete_game(self, game_id: int):
        return self.repository.delete(game_id)