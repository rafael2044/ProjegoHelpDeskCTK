from peewee import Model, CharField
from connect import db

class Prioridade(Model):
    nome_prioridade = CharField(max_length=20)
    class Meta:
        database=db