from mongoengine import Document, StringField, EmailField, ListField, EmbeddedDocument, EmbeddedDocumentField

class Profile(EmbeddedDocument):
    name = StringField()
    bio = StringField()
    profilePicture = StringField()

class Subscription(EmbeddedDocument):
    bookId = StringField()
    subscribedAt = StringField()
    expiresAt = StringField()

class User(Document):
    username = StringField(required=True, unique=True)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)  # You should hash the password
    profile = EmbeddedDocumentField(Profile)
    subscriptions = ListField(EmbeddedDocumentField(Subscription))
