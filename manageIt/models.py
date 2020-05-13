from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from manageIt import app

db = SQLAlchemy(app)


class Kindergarten(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    manager_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    kids = relationship("Kid", backref='kindergarten')


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    kindergarten = relationship("Kindergarten", backref='manager', uselist=False)


# allergicKids = db.Table('allergicKids',
#                        db.Column('kid_id', db.Integer, db.ForeignKey('kid.id')),
#                        db.Column('allergy_id', db.Integer, db.ForeignKey('typesOfAllergies.id'))
#                        )
Base = declarative_base()


class Kid(Base):
    __tablename__ = 'kid'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    birthDate = db.Column(db.Date, nullable=False)
    groupAge = db.Column(db.Integer, nullable=False)
    kindergarten_id = db.Column(db.Integer, db.ForeignKey('kindergarten.id'))
    allergies = db.relationship('typesOfAllergies', secondary='allergicKids', backref=db.backref('kid', lazy='dynamic'))


class TypesOfAllergies(Base):
    __tablename__ = 'typesOfAllergies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class AllergicKids(Base):
    __tablename__ = 'allergicKids'
    id = db.Column(db.Integer, primary_key=True)
    kid_id = db.Column(db.Integer, db.ForeignKey('kid.id'))
    allergy_id = db.Column(db.Integer, db.ForeignKey('allergy.id'))
