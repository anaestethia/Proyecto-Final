from fastapi import FastAPI
from controllers.game_controller import router as game_router
from controllers.user_controller import router as user_router
from controllers.review_controller import router as review_router
from models.database import engine, Base

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(game_router)
app.include_router(user_router)
app.include_router(review_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Game Library API"}