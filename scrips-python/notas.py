class Aluno:
    
    def __init__(self, nome, idade, matricula):
        self.__nome = nome
        self._idade = idade
        self.matricula = matricula
        self.notas = None


    def get_nome(self):
        return self.__nome


    def set_nome(self, nome):
        self.__nome = nome


    def get_idade(self):
            return self._idade


    def set_idade(self, idade):
            self._idade = idade
        

        
aluno1 = Aluno('José', 15, 123456)
print(aluno1.get_nome())
print(aluno1.get_idade())
print(aluno1.matricula)
print(aluno1.notas)
              
