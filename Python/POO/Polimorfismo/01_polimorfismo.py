class Passaro:
    def voar(self):
        print("Voando ....")

class Pardal(Passaro):
    def voar(self):
        super().voar()

class Avestrus:
    def voar(self):
        print("Avestrus não sabe voar")

def plano_voo(obj):
    obj.voar()


plano_voo(Pardal())
plano_voo(Avestrus())