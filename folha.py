class usuario:
    def __init__(self,_id, _login, _senha, _dtexpiracao):
        self.id=_id
        self.login=_login
        self.senha=_senha
        self.dtexpiracao=_dtexpiracao
        self.tpPessoa= None 
    def __str__(self):
        ret=''
        return ret


class coordenador:
    def __init__(self,id , usuario, nome, celular, email):
        self.id= id
        self.usuario= usuario
        self.nome= nome
        self.celular= celular
        self.email= email
        self.usuario.tpPessoa= self
        self.apelido='Coordenador'
    def __str__(self):
        ret= 'Eu sou um {}\n'.format(self.apelido)
        return ret


class aluno:
    def __init__(self,_id,_idusuario,_nome,_celular,_email,_RA,_foto):
        self.id=_id
        self.idusuario=_idusuario
        self.nome=_nome
        self.idusuario=_idusuario
        self.celular=_celular
        self.email=_email
        self.RA=_RA
        self.foto=_foto
    def imprime(self):
        return ("id:{}, "+
        "idusuario:{}, "+
        " nome:{}, "+
        "celular:{}, "+
        "email:{}"+
        "RA:{}"+
        "foto: {}").format(self.id,self.idusuario,self.nome,self.celular,self.email,self.RA,self.foto)
lucas= usuario('01','hastad','3223222323323','2020')    
lucascoord=coordenador('1',lucas ,'Lucas','999','email@email')
print(lucas.imprime(), lucascoord)