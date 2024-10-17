class Estudantes:
    escola = "DIO"


    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)
    
aluno01 = Estudantes("Wesllan" , 1)
aluno02 = Estudantes("Carol" , 2)

mostrar_valores(aluno01,aluno02)

aluno02.nome = "Carolina"
aluno02.matricula = 3
Estudantes.escola = "PYTHON"
aluno03 = Estudantes("Gustavo", 4,)
mostrar_valores(aluno01,aluno02, aluno03)
