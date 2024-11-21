from fastapi import FastAPI, Request, HTTPException, Depends
from controllers.game_controller import router as game_router
from models.database import engine, Base
from models.game_model import Game
from models.game_schema import Game as GameSchema, GameCreate
from sqlalchemy.orm import Session
from datetime import date
import logging
from fastapi.middleware.cors import CORSMiddleware

# Configuración del logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Crear tablas
Base.metadata.create_all(bind=engine)

# Función para agregar datos iniciales
def add_initial_data(db: Session):
    if db.query(Game).count() == 0: 
        initial_games = [
            Game(
                title="The Legend of Zelda: Breath of the Wild",
                genre="Action-Adventure",
                platform="Nintendo Switch",
                developer="Nintendo",
                release_date=date(2017, 3, 3),
                description="An open-world action-adventure game."
            ),
            # ... resto de los juegos iniciales ...
        ]
        db.add_all(initial_games)
        db.commit()

def get_db():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()

app = FastAPI(
    title="Game Library API",
    description="API para gestionar una biblioteca de juegos",
    version="1.0.0"
)

app.include_router(game_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    db = Session(bind=engine)
    add_initial_data(db)
    db.close()

app.include_router(
    game_router,
    prefix="/api/v1",
    tags=["games"]
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Game Library API"}

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Response: {response.status_code}")
    return response

@app.post("/games", response_model=GameSchema, status_code=201)
def create_game(game: GameCreate, db: Session = Depends(get_db)):
    try:
        db_game = Game(
            title=game.title,
            genre=game.genre,
            platform=game.platform,
            developer=game.developer,
            release_date=game.release_date,
            description=game.description
        )
        db.add(db_game)
        db.commit()
        db.refresh(db_game)
        logger.info("Juego creado exitosamente.")
        return db_game
    except Exception as e:
        logger.error(f"Error al crear juego: {str(e)}")
        raise HTTPException(status_code=500, detail="Error interno del servidor")

@app.get("/games/{game_id}", response_model=GameSchema, 
         responses={404: {"description": "Juego no encontrado"}})
def read_game(game_id: int, db: Session = Depends(get_db)):
    game = db.query(Game).filter(Game.id == game_id).first()
    if game is None:
        logger.error(f"Juego con ID {game_id} no encontrado.")
        raise HTTPException(status_code=404, detail="Juego no encontrado")
    return game