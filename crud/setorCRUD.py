from models.model import Setor

def adicionar_setor(nome_setor):
    setor_existe = Setor.filter(Setor.nome == nome_setor)
    
    if not setor_existe:
        if len(nome_setor)>2:
            novo_setor = Setor(nome=nome_setor)
            novo_setor.save()
            return {'mensagem':'Setor cadastrado com sucesso!', 'tipo':'sucesso'}
        else: return {'mensagem':'O nome do setor precisa conter 3 ou mais caracteres!', 'tipo':'info'}
            
    else: return {'mensagem':'O setor ja existe', 'tipo':'aviso'}
    

def selecionar_todos_setores():
    setores = [ setor for setor in Setor.select()]
    return setores

def seleciona_nome_setores():
    setores = [ setor.nome if setor is not None else '' for setor in Setor.select()]
    return setores

def selecionar_id_setor_por_nome(nome_setor):
    id_setor = Setor.get(Setor.nome==nome_setor).id
    
    return id_setor