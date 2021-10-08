"""
Módulo de configuração do servidor flask
"""
DEBUG = False

SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = "LOL"
