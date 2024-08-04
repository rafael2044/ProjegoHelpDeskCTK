from peewee import Model, CharField, ForeignKeyField, TextField, DateTimeField
from connect import db
from datetime import datetime






class Status:
    STATUS_CHOICES=(
    (0, 'Pendente'),
    (1, 'Concluido')
    )
    
    @classmethod
    def get_status_name(cls):
        return [x[-1] for x in cls.STATUS_CHOICES]
    
    @classmethod
    def get_status_id(cls, name):
        for x in cls.get_status():
            if name in x:
                return x[0]
    
    @classmethod 
    def get_status(cls):
        return cls.STATUS_CHOICES


class Privilegio:
    PRIVILEGIO_CHOICES = (
    (1, 'Administrador'),
    (2, 'Suporte'),
    (3, 'Padrao')
    )
    
    @classmethod
    def get_privilegios_name(cls):
        return [x[-1] for x in cls.PRIVILEGIO_CHOICES]

    @classmethod
    def get_privilegio_id(cls, name):
        for x in cls.get_privilegios():
            if name in x:
                return x[0]

    @classmethod
    def get_privilegios(cls):
        return cls.PRIVILEGIO_CHOICES
    
    

class Prioridade:
    PRIORIDADE_CHOICES = (
    (1, 'Baixa'),
    (2, 'Media'),
    (3, 'Alta')
    )
    @classmethod
    def get_prioridades_name(cls):
        return [x[-1] for x in cls.PRIORIDADE_CHOICES]
    
    @classmethod
    def get_prioridade_id(cls, name):
        for x in cls.get_prioridades():
            if name in x:
                return x[0]

    
    @classmethod
    def get_prioridades(cls):
        return cls.PRIORIDADE_CHOICES



class Categoria:
    CATEGORIA_CHOICES=(
        (1, 'Sistema'),
        (2, 'Equipamento'),
        (3, 'Software'),
        (4, 'Internet')
    ) 
    
    @classmethod
    def get_categorias_name(cls):
        return list(dict(cls.CATEGORIA_CHOICES).values())
    
    @classmethod
    def get_categoria_id(cls, name):
        for x in cls.get_categorias():
            if name in x:
                return x[0]
    
    @classmethod
    def get_categorias(cls):
        return cls.CATEGORIA_CHOICES
        



class Setor(Model):
    nome = CharField(max_length=50)
    class Meta:
        database=db

class Usuario(Model):
    nome = CharField()
    usuario = CharField()
    senha = CharField()
    privilegio = CharField(choices=Privilegio.get_privilegios())
    class Meta:
        database=db
        
    def get_privilegio(self):
        return dict(Privilegio.get_privilegios())[int(self.privilegio)]
        
        
class Chamado(Model):
    
    solicitante = ForeignKeyField(Usuario, backref='solicitante')
    titulo = CharField()
    setor = ForeignKeyField(Setor, backref='setores')
    categoria = CharField(choices=Categoria.get_categorias())
    prioridade = CharField(choices=Prioridade.get_prioridades())
    detalhes = TextField()
    data_abertura = DateTimeField(default=datetime.now)
    status = CharField(choices=Status.get_status())
    
    class Meta:
        database=db
        
    def get_categoria(self):
        return dict(Categoria.get_categorias())[int(self.categoria)]
    
    def get_prioridade(self):
        return dict(Prioridade.get_prioridades())[int(self.prioridade)]
    
    def get_status(self):
        return dict(Status.get_status())[int(self.status)]
    
        
class Atendimento(Model):
    chamado = ForeignKeyField(Chamado, backref='atendimento')
    suporte = ForeignKeyField(Usuario, backref='suporte')
    detalhes = TextField()
    data_atendimento = DateTimeField(default=datetime.now)
    
    class Meta:
        database=db