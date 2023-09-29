from flask_mongoengine import Document
from mongoengine.fields import StringField, IntField

class Book(Document):
    title = StringField(required=True)
    author = StringField(required=True)
    genre = StringField()

