from mongoengine import *
class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=30)
    last_name = StringField(max_length=30)