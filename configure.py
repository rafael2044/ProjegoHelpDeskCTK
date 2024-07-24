from connect import db
from models.setor import Setor
from models.prioridade import Prioridade
from models.situacao import Situacao
from models.privilegio import Privilegio
from models.usuario import Usuario
from models.categoria import Categoria
from models.chamado import Chamado

PRIORIDADES = ('Baixa', 'Media', 'Alta')
SITUACAO = ('Pendente', 'Concluido')
PRIVILEGIOS = ('Padrao', 'Suporte', 'Administrador')
CATEGORIAS = ("Sistema", 'Equipamento', 'Software', 'Internet')
USUARIO_ADM = [('---', 'sar', 'sist', 3)]

def inserir_dados_padroes():
    try:
        if not Prioridade.select().execute():
            for p in PRIORIDADES:
                prioridade = Prioridade(nome_prioridade = p)
                prioridade.save()
        
        if not Situacao.select().execute():
            for s in SITUACAO:
                situacao = Situacao(nome_situacao = s)
                situacao.save()
        
        if not Privilegio.select().execute():
            for pri in PRIVILEGIOS:
                privilegio = Privilegio(nome_privilegio = pri)
                privilegio.save()
                
        if not Categoria.select().execute():
            for cat in CATEGORIAS:
                categoria = Categoria(nome_categoria = cat)
                categoria.save()
        if not Usuario.select().execute():
            for usuario in USUARIO_ADM:
                new_usuario = Usuario(nome_usuario = usuario[0], login_usuario = usuario[1], senha_usuario = usuario[2],
                                  privilegio_usuario = usuario[3])
                new_usuario.save()
    except Exception as e:
        print(f"Erro ao inserir dados padrões:{e}")
    
def criar_database(db):
    try:
        db.create_tables([Setor, Prioridade, Situacao, Privilegio, Usuario, Categoria, Chamado])
        inserir_dados_padroes()
    except Exception as e:
        print(f"Erro ao inicializar tabelas: {e}")
criar_database(db)
    
