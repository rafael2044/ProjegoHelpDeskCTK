from peewee import Model, CharField, ForeignKeyField
from models.privilegio import Privilegio
from connect import db

class Usuario(Model):
    nome_usuario = CharField()
    login_usuario = CharField()
    senha_usuario = CharField()
    privilegio_usuario = ForeignKeyField(Privilegio, backref='privilegios')
    class Meta:
        database=db