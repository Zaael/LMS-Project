class Entrega ():
    def __init__(self, Aluno, AtividadeVinculada, titulo, resposta ):
        self.idEntrega=int
        self.titulo= titulo
        self.resposta= resposta
        self.dtEntrega= 'dtEntrega'
        self.Status='Entregue'
        self.Aluno.idAluno= int
        self.idAtividadeVinculada=int
        self.idProfessor=int
        self.Nota=0
        self.DtAvaliacao='00/00/2200'
        self.Obs=""
    def __str__(self):
        return 'Etregue, sua nota: {}'.format(self.Nota)





class Mensagem():
    def __init__(self, Aluno, Professor, conteudo):
        self.idMensagem=0
        self.Aluno.idAluno=int
        self.Professor.idProfessor=int
        self.Assunto={}
        self.Referencia={}
        self.Conteudo=input()
        self.Status=('Enviado', 'Lido', 'Respondido')
        self.DtEnvio='00/00/2000'
        self.DtResposta='00/00/200'
        self.Resposta=input()
    def __str__(self):
        return "Mensagem"

