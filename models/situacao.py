from peewee import Model, CharField
from connect import db

class Situacao(Model):
    nome_situacao = CharField(max_length=20)
    class Meta:
        database=db