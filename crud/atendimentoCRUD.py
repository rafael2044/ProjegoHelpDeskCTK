from models.model import Chamado, Atendimento

def atender_chamado_id(id_chamado, suporte, detalhes):
    chamado = Chamado.get_by_id(id_chamado)
    
    if len(detalhes) > 9:
        atendimento = Atendimento(chamado=id_chamado,suporte=suporte,detalhes=detalhes)
        chamado.status = 1
        atendimento.save()
        chamado.save()
        return {"mensagem":"Chamado atendido com sucesso!", 'tipo':'sucesso'}
    else:
        return {"mensagem":"A descricao do atendimento precisa ter 10 ou mais caracteres", 'tipo':'info'}

def selecionar_todos_atendimentos():
    atendimentos = [atendimento for atendimento in Atendimento.select()]
    return atendimentos


def selecionar_atendimentos_suporte(id_suporte):
    atendimentos = [atendimento for atendimento in Atendimento.select().filter(Atendimento.suporte == id_suporte)]
    return atendimentos