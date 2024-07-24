from peewee import Model, CharField
from connect import db

class Categoria(Model):
    nome_categoria = CharField(max_length=20)
    class Meta:
        database=db