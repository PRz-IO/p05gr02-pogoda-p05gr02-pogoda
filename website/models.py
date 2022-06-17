from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy.schema import ForeignKey
from flask_sqlalchemy import SQLAlchemy

Miasto_Uzytkownika = db.Table('Miasto_Uzytkownika', #https://www.youtube.com/watch?v=47i-jzrrIGQ
    db.Column('id_uzytkownika', db.Integer, db.ForeignKey('user.id')),
    db.Column('id_miasta', db.Integer, ForeignKey("miasto.id"))
)
Preferencje_Uzytkownika = db.Table('Preferencje_Uzytkownika',
    db.Column('id_uzytkownika', db.Integer, db.ForeignKey('user.id')),
    db.Column('id_jednostki', db.Integer, ForeignKey("jednostka.id"))
)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable = False)
    username = db.Column(db.String(128), unique=True, nullable = False)
    password = db.Column(db.String(128), nullable = False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    miasta = db.relationship('Miasto', secondary=Miasto_Uzytkownika, backref='uzytkownicy')
    preferencje = db.relationship('Jednostka', secondary=Preferencje_Uzytkownika, backref='uzytkownicy')

class Kraj(db.Model): #https://www.youtube.com/watch?v=VVX7JIWx-ss
    id = db.Column(db.Integer, primary_key=True)
    nazwa_kraju = db.Column(db.String(64), unique=True, nullable = False)
    miasta = db.relationship('Miasto', backref = 'kraj')

class Miasto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nazwa_miasta = db.Column(db.String(64), nullable = False)
    id_kraju = db.Column(db.Integer, db.ForeignKey("kraj.id"), nullable = False)
    pogoda_dzienna = db.relationship('PogodaDzienna', backref = 'miasto')
    pogoda_godzinowa = db.relationship('PogodaGodzinowa', backref = 'miasto')

class Atrybut(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nazwa_atrybutu = db.Column(db.String(64), unique=True, nullable = False)
    jednostki = db.relationship('Jednostka', backref='atrybut')

class Jednostka(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nazwa_jednostki = db.Column(db.String(64), nullable = False) 
    id_atrybutu = db.Column(db.Integer, ForeignKey("atrybut.id")) 

class stanpogody(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stan_pogody = db.Column(db.String(64), unique=True, nullable = False)
    pogoda_dzienna = db.relationship('PogodaDzienna', backref = 'stanpogody')
    pogoda_godzinowa = db.relationship('PogodaGodzinowa', backref = 'stanpogody')

class PogodaDzienna(db.Model):#pewnie zamiast min max temp lepiej wziąć temperatury dla poranka, południa, wieczora i nocy
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime(timezone=True)) 
    min_temp = db.Column(db.Integer)
    max_temp = db.Column(db.Integer)
    id_miasta = db.Column(db.Integer, ForeignKey("miasto.id"), nullable = False)
    id_stan_pogody = db.Column(db.Integer, ForeignKey("stanpogody.id"), nullable = False)
    rano = db.Column(db.Integer)
    poludnie = db.Column(db.Integer)
    wieczor = db.Column(db.Integer)
    noc = db.Column(db.Integer)
    opad = db.Column(db.Integer)

class PogodaGodzinowa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #godzina = db.Column(db.DateTime(True))
    data = db.Column(db.DateTime(timezone=True))
    temperatura = db.Column(db.Integer)
    predkosc_wiatru = db.Column(db.Integer)
    cisnienie = db.Column(db.Integer)
    id_miasta = db.Column(db.Integer, ForeignKey("miasto.id"), nullable = False)
    id_stan_pogody = db.Column(db.Integer, ForeignKey("stanpogody.id"), nullable = False)



