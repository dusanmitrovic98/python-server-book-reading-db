from mongoengine import Document, ReferenceField, StringField
from app.models.chapter import Chapter
from app.models.user import User

class History(Document):
    user = ReferenceField(User)
    chapter = ReferenceField(Chapter)
    timestamp = StringField()
