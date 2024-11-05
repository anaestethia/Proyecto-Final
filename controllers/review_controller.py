from fastapi import APIRouter
from services.review_service import ReviewService
from models.review_schema import Review, ReviewCreate

router = APIRouter()
service = ReviewService()

@router.post("/reviews/", response_model=Review)
def create_review(review: ReviewCreate):
    return service.create_review(review)

@router.get("/reviews/{game_id}", response_model=list[Review])
def get_reviews(game_id: int):
    return service.get_reviews(game_id)