from mongoengine import Document, StringField, DateTimeField, FloatField, IntField

class Book(Document):
    title = StringField(required=True)
    author = StringField()
    genre = StringField()
    publicationDate = DateTimeField()
    description = StringField()
    coverImage = StringField()
    averageRating = FloatField(default=0.0)
    totalRatingsCount = IntField(default=0)
