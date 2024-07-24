from peewee import Model, CharField, ForeignKeyField, DateTimeField, TextField
from models.setor import Setor
from models.prioridade import Prioridade
from models.situacao import Situacao
from models.usuario import Usuario
from models.categoria import Categoria
from connect import db
import datetime

class Chamado(Model):
    usuario_solicitante = ForeignKeyField(Usuario, backref='usuario_solicitante')
    titulo = CharField()
    setor = ForeignKeyField(Setor, backref='setores')
    categoria = ForeignKeyField(Categoria, backref='categorias')
    prioridade = ForeignKeyField(Prioridade, backref='prioridades')
    detalhes = TextField()
    data_abertura = DateTimeField(default=datetime.datetime.now)
    situacao = ForeignKeyField(Situacao, backref='situacoes')
    data_fechamento = DateTimeField()
    suporte_atendimento = ForeignKeyField(Usuario, backref='suporte_atendimento')
    descricao_atendimento = TextField()
    
    class Meta:
        database=db