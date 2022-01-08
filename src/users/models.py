from src.databse import db, Base
from uuid import uuid4


class User(Base):
    __tablename__ = 'users'

    id = db.Column(db.String(50), primary_key=True, default=uuid4)
    email = db.Column(db.String(254), unique=True)
    name = db.Column(db.String(100))
    location = db.Column(db.String(100))
