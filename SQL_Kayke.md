-- Kayke Bento Aleixo 1801013
-- Classes: Disciplina, SolicitacaoMatricula, Atividade
--

CREATE TABLE Disciplina 
(
ID TINYINT IDENTITY, 
Nome VARCHAR(35) NOT NULL, 
Data DATE NOT NULL CONSTRAINT dfData DEFAULT (GETDATE()), 
Status CHAR(7) NOT NULL  CONSTRAINT dfStatus DEFAULT 'Aberta', 
PlanoDeEnsino VARCHAR(50) NOT NULL,
CargaHoraria TINYINT NOT NULL, 
Competencias VARCHAR(50) NOT NULL,
Habilidades VARCHAR(50) NOT NULL,
Ementa VARCHAR(50) NOT NULL,
ConteudoProgramatico VARCHAR(50) NOT NULL,
BibliografiaBasica VARCHAR(50) NOT NULL,
BibliografiaComplementar VARCHAR(50) NOT NULL,
PercentualPratico TINYINT NOT NULL, 
PercentualTeorico TINYINT NOT NULL, 
IdCoordenador TINYINT NOT NULL, 

CONSTRAINT pkDisciplina PRIMARY KEY (ID),
CONSTRAINT uqDisciplinaNome UNIQUE (Nome),
CONSTRAINT ckStatus CHECK (Status = 'Aberta' OR Status = 'Fechada'),
CONSTRAINT ckCargaHr CHECK (CargaHoraria = 40 OR CargaHoraria = 80),
CONSTRAINT ckPercPratico CHECK (PercentualPratico >= 0 AND PercentualPratico <= 100),
CONSTRAINT ckPercTeorico CHECK (PercentualTeorico >=0 AND PercentualTeorico <=100),
CONSTRAINT fkDisciplina_IdCoord FOREIGN KEY (IdCoordenador) REFERENCES Coordenador(ID)
);



CREATE TABLE SolicitacaoMatricula 
(
ID TINYINT IDENTITY,
IdAluno INT NOT NULL, 
IdDisciplinaOfertada TINYINT NOT NULL, 
DtSolicitacao DATE NOT NULL CONSTRAINT dfDtSolicitacao DEFAULT (GETDATE()), 
IdCoordenador TINYINT, 
Status char(10) CONSTRAINT dfStatus DEFAULT 'Solicitada', 

CONSTRAINT pkSoliciMatricula PRIMARY KEY (ID),
CONSTRAINT fkSoliciMat_IdAluno FOREIGN KEY (IdAluno) REFERENCES Aluno(ID),
CONSTRAINT fkSoliciMat_IdDiscOfert FOREIGN KEY (IdDisciplinaOfertada) REFERENCES DisciplinaOfertada(ID),
CONSTRAINT fkSoliciMat_IdCoord FOREIGN KEY (IdCoordenador) REFERENCES Coordenador(ID),
CONSTRAINT ckStatus CHECK (Status = 'Solicitada' OR Status = 'Aprovada' OR Status = 'Rejeitada' OR Status = 'Cancelada'),
);


CREATE TABLE Atividade (
ID TINYINT IDENTITY, 
Titulo VARCHAR(30) NOT NULL,
Descricao VARCHAR(50),
Conteudo VARCHAR(50) NOT NULL, 
Tipo VARCHAR(15) NOT NULL, 
Extras VARCHAR(30),
IdProfessor TINYINT NOT NULL, 

CONSTRAINT pkAtividade PRIMARY KEY (ID),
CONSTRAINT uqTitulo UNIQUE (TItulo),
CONSTRAINT ckTipo CHECK (Tipo = 'Reposta Aberta' OR Tipo= 'Teste'),
CONSTRAINT fkAtividade_IdProf FOREIGN KEY (IdProfessor) REFERENCES Professor(ID)
);
