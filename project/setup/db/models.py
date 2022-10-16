from sqlalchemy import func

from project.setup.db import db


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created = db.Column(db.DateTime, nullable=False, default=func.now())
    updated = db.Column(db.DateTime, default=func.now(), onupdate=func.now())
