from models.model import Chamado

def adicionar_chamado(solicitante:int, titulo:str,setor:int, categoria:int, prioridade:int,
                      detalhes:str, status=0):
    
    if len(titulo)>10:
        if len(detalhes) > 10:
            novo_chamado = Chamado(solicitante=solicitante, titulo=titulo,
                                   setor=setor, categoria=categoria,
                                   prioridade=prioridade, detalhes=detalhes, 
                                   status=status)
            novo_chamado.save()
            return {'mensagem':f'O chamado foi aberto! Num. {novo_chamado.id}', 'tipo':'sucesso'}
        else: return {'mensagem':'Os detalhes precisam ter 10 ou mais caracteres!', 'tipo':'info'}
    else: return {'mensagem':'O titulo precisa ter 10 ou mais caracteres!', 'tipo':'info'}
 
def selecionar_todos_chamados():
    chamados = [chamado for chamado in Chamado.select()]
    return chamados
   
def selecionar_chamado_solitado_por(id_usuario):
    chamados = [chamado for chamado in Chamado.select().filter(Chamado.solicitante == id_usuario)]
    return chamados
    
def selecionar_chamado_atendido_por(id_suporte):
    chamados = [chamado for chamado in Chamado.select().filter(Chamado.suporte == id_suporte)]
    return chamados

