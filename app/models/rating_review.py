from mongoengine import Document, ReferenceField, StringField, IntField
from app.models.bookmark import Bookmark
from app.models.user import User

class RatingReview(Document):
    user = ReferenceField(User)
    book = ReferenceField(Bookmark)
    rating = IntField()
    review = StringField()
    timestamp = StringField()
