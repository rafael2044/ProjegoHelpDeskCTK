from peewee import Model, CharField
from connect import db

class Setor(Model):
    nome_setor = CharField(max_length=50)
    class Meta:
        database=db