from mongoengine import Document, ReferenceField, FloatField, StringField
from app.models.user import User

class Payment(Document):
    user = ReferenceField(User)
    amount = FloatField()
    paymentMethod = StringField()
    timestamp = StringField()
