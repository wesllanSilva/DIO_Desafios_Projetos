class Pessoa:
    def __init__(self,nome=None,idade=None):
        self.nome = nome
        self.idade = idade

    
    @classmethod
    def criar_da_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)
    
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18
    
p = Pessoa.criar_da_data_nascimento(1990,3,20,'Wesllan')
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(10))
print(Pessoa.e_maior_idade(25))