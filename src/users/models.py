from src.databse import db, Base
from uuid import uuid4


# User table
class User(Base):
    __tablename__ = 'users'

    id = db.Column(db.String(50), primary_key=True, nullable=False, default=uuid4)
    email = db.Column(db.String(254), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(80))
