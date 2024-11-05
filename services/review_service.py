from repositories.review_respository import ReviewRepository
from models.review_model import Review as ReviewModel
from models.review_schema import ReviewCreate

class ReviewService:
    def __init__(self):
        self.repository = ReviewRepository()

    def create_review(self, review: ReviewCreate):
        review_model = ReviewModel(**review.dict())  # Convertir a modelo de SQLAlchemy
        return self.repository.create(review_model)

    def get_reviews(self, game_id: int):
        return self.repository.get_by_game(game_id)