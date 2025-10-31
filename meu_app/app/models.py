from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True)
    senha_hash = db.Column(db.String(128))
    tipo_usuario = db.Column(db.String(20))
    clinica_id = db.Column(db.Integer, db.ForeignKey('clinica.id'))
    tutor_id = db.Column(db.Integer, db.ForeignKey('tutor.id'))

class Clinica(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120))
    cnpj = db.Column(db.String(20))
    endereco = db.Column(db.String(200))
    telefone = db.Column(db.String(20))
    usuarios = db.relationship('User', backref='clinica', lazy=True)
    animais = db.relationship('Animal', backref='clinica', lazy=True)

class Tutor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120))
    cpf = db.Column(db.String(20))
    telefone = db.Column(db.String(20))
    animais = db.relationship('Animal', backref='tutor', lazy=True)

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120))
    especie = db.Column(db.String(50))
    raca = db.Column(db.String(50))
    idade = db.Column(db.Integer)
    tutor_id = db.Column(db.Integer, db.ForeignKey('tutor.id'))
    clinica_id = db.Column(db.Integer, db.ForeignKey('clinica.id'))
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)