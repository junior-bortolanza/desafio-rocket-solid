from abc import ABC, abstractmethod

class AprovaExame(ABC):

    @abstractmethod
    def aprovar_solicitacao_exame(self, exame): pass

    @abstractmethod
    def verificar_condicoes_exame(self, exame): pass

class AprovaExameSangue(AprovaExame):
    def aprovar_solicitacao_exame(self, exame):
        if self.verificar_condicoes_exame(exame):
            print("Exame sanguínio aprovado")
    
    def verificar_condicoes_exame(self, exame):
        pass

class AprovaExameRaiox(AprovaExame):
    def aprovar_solicitacao_exame(self, exame):
        if self.verificar_condicoes_exame(exame):
            print("Raio-X aprovado!")
    
    def verificar_condicoes_exame(self, exame):
        pass

class Exame:
    def __init__(self, tipo):
        self.tipo = tipo

exame_sangue = Exame("Sangue")
exame_raio_x = Exame("Raio-x")

aprovador_sangue = AprovaExameSangue()
aprovador_raio_x = AprovaExameRaiox()

aprovador_sangue.aprovar_solicitacao_exame(exame_sangue)
aprovador_raio_x.aprovar_solicitacao_exame(exame_raio_x)
