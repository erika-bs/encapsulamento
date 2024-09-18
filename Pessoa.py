class Pessoa():
    def __init__(self,nome,idade):
        # encapsulamento
        #self.__nome = nome // makes it private
        #self._nome = nome // protected // useless for python
        self.__nome = nome
        self.idade = idade
       # print("private:",self.__nome)

    def getExibir(self):
        self.nomeCompleto = self.__nome

    def setExibir(self):
        return self.nomeCompleto