from fastapi import APIRouter
from services.game_service import GameService
from models.game_schema import Game, GameCreate

router = APIRouter()
service = GameService()

@router.post("/games/", response_model=Game)
def create_game(game: GameCreate):
    return service.create_game(game)

@router.get("/games/", response_model=list[Game])
def get_games():
    return service.get_all_games()

@router.get("/games/{game_id}", response_model=Game)
def get_game(game_id: int):
    return service.get_game(game_id)

@router.put("/games/{game_id}", response_model=Game)
def update_game(game_id: int, game: GameCreate):
    return service.update_game(game_id, game)

@router.delete("/games/{game_id}", response_model=Game)
def delete_game(game_id: int):
    return service.delete_game(game_id)