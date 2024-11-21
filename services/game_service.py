from sqlalchemy.orm import Session
from models.game_model import Game as GameModel
from models.game_schema import GameCreate
from fastapi import HTTPException

class GameService:
    def __init__(self, db: Session):
        self.db = db

    def create_game(self, game: GameCreate):
        db_game = GameModel(
            name=game.name,
            genre=game.genre
        )
        self.db.add(db_game)
        self.db.commit()
        self.db.refresh(db_game)
        return db_game

    def get_all_games(self):
        return self.db.query(GameModel).all()

    def get_game(self, game_id: int):
        return self.db.query(GameModel).filter(GameModel.id == game_id).first()

    def update_game(self, game_id: int, game: GameCreate):
        db_game = self.db.query(GameModel).filter(GameModel.id == game_id).first()
        if db_game:
            db_game.name = game.name
            db_game.genre = game.genre
            self.db.commit()
            self.db.refresh(db_game)
            return db_game
        else:
            raise HTTPException(status_code=404, detail="Juego no encontrado")

    def delete_game(self, game_id: int):
        db_game = self.db.query(GameModel).filter(GameModel.id == game_id).first()
        if db_game:
            self.db.delete(db_game)
            self.db.commit()
            return True
        else:
            raise HTTPException(status_code=404, detail="Juego no encontrado")