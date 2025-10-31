import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'chave-super-secreta')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///instance/app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False