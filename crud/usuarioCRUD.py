from models.model import Usuario


def adicionar_usuario(nome:str, usuario:str, senha:str, privilegio:int):
    usuario_existe = Usuario.filter(Usuario.nome == nome,
                                    Usuario.usuario == usuario)

    if not usuario_existe:
        if len(senha) > 2:
            if len(nome) > 10:
                novo_usuario = Usuario(nome = nome, usuario=usuario,
                                   senha = senha, privilegio = privilegio)
                novo_usuario.save()
                return {'mensagem':'Usuario cadastrado com sucesso','tipo':'sucesso'}
            else: return {'mensagem':'O nome precisa ter 10 ou mais caracteres!','tipo':'info'}
                
        else: return {'mensagem':'A senha precisa ter 3 ou mais caracteres!','tipo':'info'}
            
    else:
        return {'mensagem':'O usuario ou o login ja existe!','tipo':'aviso'}
    
def selecionar_todos_usuarios():
    usuarios = [usuario for usuario in Usuario.select()]
    
    return usuarios


def quantidade_usuarios():
    return len(Usuario.select())

