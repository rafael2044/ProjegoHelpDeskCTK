from peewee import Model, CharField
from connect import db

class Privilegio(Model):
    nome_privilegio = CharField(max_length=50)
    class Meta:
        database=db