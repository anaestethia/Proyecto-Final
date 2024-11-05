from models.database import SessionLocal
from models.review_model import Review

class ReviewRepository:
    def __init__(self):
        self.db = SessionLocal()

    def create(self, review: Review):
        self.db.add(review)
        self.db.commit()
        self.db.refresh(review)
        return review

    def get_by_game(self, game_id: int):
        return self.db.query(Review).filter(Review.game_id == game_id).all()