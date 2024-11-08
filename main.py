from fastapi import FastAPI
from controllers.game_controller import router as game_router
from models.database import engine, Base
from models.game_model import Game
from sqlalchemy.orm import Session
from datetime import date


Base.metadata.create_all(bind=engine)

def add_initial_data(db: Session):
    if db.query(Game).count() == 0: 
        initial_games = [
            Game(title="The Legend of Zelda: Breath of the Wild", genre="Action-Adventure", platform="Nintendo Switch", developer="Nintendo", release_date=date(2017, 3, 3), description="An open-world action-adventure game."),
            Game(title="God of War", genre="Action-Adventure", platform="PlayStation 4", developer="Santa Monica Studio", release_date=date(2018, 4, 20), description="An action-adventure game based on Norse mythology."),
            Game(title="Minecraft", genre="Sandbox", platform="Multiple", developer="Mojang Studios", release_date=date(2011, 11, 18), description="A sandbox game that allows players to build and explore virtual worlds."),
            Game(title="The Witcher 3: Wild Hunt", genre="RPG", platform="PC, PS4, Xbox One", developer="CD Projekt Red", release_date=date(2015, 5, 19), description="An open-world RPG set in a fantasy universe."),
            Game(title="Red Dead Redemption 2", genre="Action-Adventure", platform="PC, PS4, Xbox One", developer="Rockstar Games", release_date=date(2018, 10, 26), description="An epic tale of life in America’s unforgiving heartland."),
            Game(title="Dark Souls III", genre="Action RPG", platform="PC, PS4, Xbox One", developer="FromSoftware", release_date=date(2016, 3, 24), description="A dark fantasy action RPG known for its challenging gameplay."),
            Game(title="Super Mario Odyssey", genre="Platform", platform="Nintendo Switch", developer="Nintendo", release_date=date(2017, 10, 27), description="A 3D platform game featuring Mario on a globe-trotting adventure."),
            Game(title="Fortnite", genre="Battle Royale", platform="Multiple", developer="Epic Games", release_date=date(2017, 7, 25), description="A free-to-play battle royale game with building mechanics."),
            Game(title="Overwatch", genre="First-Person Shooter", platform="PC, PS4, Xbox One", developer="Blizzard Entertainment", release_date=date(2016, 5, 24), description="A team-based multiplayer first-person shooter."),
            Game(title="Hollow Knight", genre="Metroidvania", platform="PC, Nintendo Switch", developer="Team Cherry", release_date=date(2017, 2, 24), description="A challenging action-adventure game set in a beautifully hand-drawn world."),
        ]
        db.add_all(initial_games)
        db.commit()

app = FastAPI()

@app.on_event("startup")
def startup_event():
    db = Session(bind=engine)
    add_initial_data(db)
    db.close()

app.include_router(game_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Game Library API"}