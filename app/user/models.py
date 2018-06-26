from flask_login import UserMixin
from app.ext import db


class User(db.Model,UserMixin):
    uid=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(64),index=True,unique=True,nullable=False)
    password=db.Column(db.String(64),nullable=False)
    email=db.Column(db.String(100),nullable=False)


