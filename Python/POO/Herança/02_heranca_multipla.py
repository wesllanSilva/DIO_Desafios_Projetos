class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f"{chave}={valor}" for chave, valor in self.__dict__.items() ])}"

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw) 

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)


class Gato(Mamifero):
    pass

class Onitorrinco(Mamifero,Ave):
    def __init__(self, nro_patas, cor_pelo, cor_bico):
        super().__init__(nro_patas=nro_patas, cor_pelo=cor_pelo,cor_bico=cor_bico)

gato = Gato(nro_patas=4, cor_pelo="Branca")
print(gato)


onitorrinco= Onitorrinco(nro_patas=2, cor_pelo="Cinza", cor_bico="amarelo")
print(onitorrinco)