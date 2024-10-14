class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando motor...")
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f"{chave}={valor}" for chave, valor in self.__dict__.items() ])}"

   
    

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__( cor, placa, numero_rodas)

        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'SIM' if self.carregado else 'NÃO'} estou carregado")
        

moto = Motocicleta("Vermelha", "ABC-2024", 2)
print(moto)
moto.ligar_motor()
caminhao = Caminhao("amarelo", "PPP-1234", 8, False)
caminhao.ligar_motor()
caminhao.esta_carregado()
print(caminhao)