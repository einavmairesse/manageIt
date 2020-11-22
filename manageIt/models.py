from flask_sqlalchemy import SQLAlchemy
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
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    kindergarten = relationship("Kindergarten", backref='manager', uselist=False)


allergicKids = db.Table('allergicKids',
                        db.Column('kid_id', db.Integer, db.ForeignKey('kid.id')),
                        db.Column('allergy_id', db.Integer, db.ForeignKey('typesOfAllergies.id')),
                        db.PrimaryKeyConstraint('kid_id', 'allergy_id')
                        )

missingKidsItems = db.Table('missingKidsItems',
                        db.Column('kid_id', db.Integer, db.ForeignKey('kid.id')),
                        db.Column('item_id', db.Integer, db.ForeignKey('typesOfKidsItems.id')),
                       db.PrimaryKeyConstraint('kid_id', 'item_id')
                       )


class Kid(db.Model):
    __tablename__ = 'kid'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    birthDate = db.Column(db.Date, nullable=False)
    groupAge = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    kids_birth_id = db.Column(db.Integer, nullable=False, unique=True)
    kindergarten_id = db.Column(db.Integer, db.ForeignKey('kindergarten.id'))
    allergies = db.relationship('TypesOfAllergies', secondary=allergicKids, backref=db.backref('kid', lazy='dynamic'))
    missing_items = db.relationship('TypesOfKidsItems', secondary=missingKidsItems, backref=db.backref('kid', lazy='dynamic'))
    reports = db.relationship('ReportsOnTheChildren', backref='kid')
    attendance = db.relationship('KidsAttendanceTable', backref='kid')


class TypesOfAllergies(db.Model):
    __tablename__ = 'typesOfAllergies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class TypesOfKidsItems(db.Model):
    __tablename__ = 'typesOfKidsItems'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class ReportsOnTheChildren(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kid_id = db.Column(db.Integer, db.ForeignKey('kid.id'))
    report = db.Column(db.String(1000), nullable=False)
    date = db.Column(db.Date, nullable=False)


class KidsAttendanceTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kid_id = db.Column(db.Integer, db.ForeignKey('kid.id'))
    reason_of_absence = db.Column(db.String(1000))
    days_of_absence = db.Column(db.Integer, nullable=False)
    date_of_absence = db.Column(db.Date, nullable=False)
