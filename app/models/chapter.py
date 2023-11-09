from mongoengine import Document, ReferenceField, StringField, IntField
from app.models.book import Book

class Chapter(Document):
    book = ReferenceField(Book)
    title = StringField()
    content = StringField()  # Store text content or HTML here
    order = IntField()
