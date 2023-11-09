from mongoengine import Document, ReferenceField, StringField
from app.models.book import Book
from app.models.user import User

class Favorite(Document):
    user = ReferenceField(User)
    book = ReferenceField(Book)
    timestamp = StringField()
