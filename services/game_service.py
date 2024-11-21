from sqlalchemy.orm import Session
from models.game_model import Game
from models.game_schema import GameCreate
import logging

logger = logging.getLogger(__name__)

class GameService:
    def __init__(self, db: Session):
        self.db = db

    def create_game(self, game: GameCreate):
        try:
            db_game = Game(
                title=game.title,
                genre=game.genre,
                platform=game.platform,
                developer=game.developer,
                release_date=game.release_date,
                description=game.description
            )
            self.db.add(db_game)
            self.db.commit()
            self.db.refresh(db_game)
            return db_game
        except Exception as e:
            logger.error(f"Error en create_game: {str(e)}")
            self.db.rollback()
            raise

    def get_game(self, game_id: int):
        return self.db.query(Game).filter(Game.id == game_id).first()

    def get_all_games(self):
        return self.db.query(Game).all()

    def update_game(self, game_id: int, game: GameCreate):
        db_game = self.get_game(game_id)
        if db_game:
            db_game.title = game.title
            db_game.genre = game.genre
            db_game.platform = game.platform
            db_game.developer = game.developer
            db_game.release_date = game.release_date
            db_game.description = game.description
            self.db.commit()
            self.db.refresh(db_game)
        return db_game

    def delete_game(self, game_id: int):
        db_game = self.get_game(game_id)
        if db_game:
            self.db.delete(db_game)
            self.db.commit()
        return db_game