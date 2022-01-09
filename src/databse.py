import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


# Base Model(Mixin)

class Base(db.Model):
    __abstract__ = True
    created_on = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=datetime.datetime.utcnow())
