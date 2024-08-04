from connect import db
from models.model import Usuario, Setor, Chamado, Atendimento


USUARIO_ADM = [('---', 'sar', 'sist', 1)]

def inserir_dados_padroes():
    try:
        if not Usuario.select().execute():
            for usuario in USUARIO_ADM:
                new_usuario = Usuario(nome = usuario[0], usuario = usuario[1], senha = usuario[2],
                                  privilegio = usuario[3])
                new_usuario.save()
    except Exception as e:
        print(f"Erro ao inserir dados padrões:{e}")
    
def criar_database(db):
    try:
        db.create_tables([Setor, Usuario,Chamado, Atendimento])
        inserir_dados_padroes()
    except Exception as e:
        print(f"Erro ao inicializar tabelas: {e}")
criar_database(db)
    
