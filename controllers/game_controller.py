from fastapi import APIRouter, HTTPException, Depends
from services.game_service import GameService
from models.game_schema import Game, GameCreate
from models.database import get_db
from sqlalchemy.orm import Session
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

@router.post("/games/", response_model=Game, status_code=201)
def create_game(game: GameCreate, db: Session = Depends(get_db)):
    try:
        service = GameService(db)
        created_game = service.create_game(game)
        logger.info(f"Juego creado exitosamente: {created_game.title}")
        return created_game
    except Exception as e:
        logger.error(f"Error al crear juego: {str(e)}")
        raise HTTPException(status_code=500, detail="Error interno del servidor")

@router.get("/games/", response_model=list[Game])
def get_games(db: Session = Depends(get_db)):
    try:
        service = GameService(db)
        return service.get_all_games()
    except Exception as e:
        logger.error(f"Error al obtener juegos: {str(e)}")
        raise HTTPException(status_code=500, detail="Error interno del servidor")

@router.get("/games/{game_id}", response_model=Game)
def get_game(game_id: int, db: Session = Depends(get_db)):
    try:
        service = GameService(db)
        game = service.get_game(game_id)
        if game is None:
            logger.warning(f"Juego con ID {game_id} no encontrado")
            raise HTTPException(status_code=404, detail="Juego no encontrado")
        return game
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error al obtener juego {game_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Error interno del servidor")

@router.put("/games/{game_id}", response_model=Game)
def update_game(game_id: int, game: GameCreate, db: Session = Depends(get_db)):
    try:
        service = GameService(db)
        updated_game = service.update_game(game_id, game)
        if updated_game is None:
            logger.warning(f"Juego con ID {game_id} no encontrado para actualizar")
            raise HTTPException(status_code=404, detail="Juego no encontrado")
        return updated_game
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error al actualizar juego {game_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Error interno del servidor")

@router.delete("/games/{game_id}", response_model=Game)
def delete_game(game_id: int, db: Session = Depends(get_db)):
    try:
        service = GameService(db)
        deleted_game = service.delete_game(game_id)
        if deleted_game is None:
            logger.warning(f"Juego con ID {game_id} no encontrado para eliminar")
            raise HTTPException(status_code=404, detail="Juego no encontrado")
        return deleted_game
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error al eliminar juego {game_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Error interno del servidor")

