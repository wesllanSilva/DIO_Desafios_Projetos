from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):

    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass
    
    @abstractproperty
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV ...")
        print("TV Ligada")

    def desligar(self):
        print("Desigando a TV ...")
        print("TV desligada")

    @property
    def marca(self):
        return "LG"

class ControleRadio(ControleRemoto):
    def ligar(self):
        print("Ligando o rádio ...")
        print("Rádio Ligado")

    def desligar(self):
        print("Desigando o rádio ...")
        print("Rádio desligado")

    @property
    def marca(self):
        return "OAC"

controle =  ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

controle = ControleRadio()
controle.ligar()
controle.desligar()
print(controle.marca)
