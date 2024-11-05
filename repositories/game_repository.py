from models.database import SessionLocal
from models.game_model import Game

class GameRepository:
    def __init__(self):
        self.db = SessionLocal()

    def create(self, game: Game):
        self.db.add(game)
        self.db.commit()
        self.db.refresh(game)
        return game

    def get_all(self):
        return self.db.query(Game).all()

    def get(self, game_id: int):
        return self.db.query(Game).filter(Game.id == game_id).first()

    def update(self, game_id: int, game: Game):
        db_game = self.get(game_id)
        for key, value in game.dict().items():
            setattr(db_game, key, value)
        self.db.commit()
        return db_game

    def delete(self, game_id: int):
        db_game = self.get(game_id)
        self.db.delete(db_game)
        self.db.commit()
        return db_game