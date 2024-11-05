from fastapi import APIRouter
from services.user_service import UserService
from models.user_schema import User, UserCreate

router = APIRouter()
user_service = UserService()

@router.post("/users/signup", response_model=User)
def signup(user: UserCreate):
    return user_service.create_user(user)

@router.post("/users/login")
def login(username: str, password: str):
    return user_service.authenticate_user(username, password)

@router.get("/users/{user_id}/favorites")
def get_favorites(user_id: int):
    return user_service.get_favorites(user_id)