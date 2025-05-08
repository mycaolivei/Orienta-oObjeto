class Pessoa():
    def __init__(self, nome, idade, peso):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.dormindo=False
        self.falando=False
        self.comendo=False
    def falar(self):
        if self.falando==True:
            print(f"{self.nome} está falando")
        elif self.dormindo==True:
            print(f"Não pode falar pois está dormindo")

        elif self.comendo==True:
            print(f"{self.nome} não pode faalr pois está comendo")
        else:
            self.falando = True
            print(f"{self.nome} começou a falar")

    def comer(self, comida):
        if self.comendo==True:
            print(f"{self.nome} está comendo")
        elif self.dormindo==True:
            print(f"{self.nome} não pode dormir pois está comendo")
        elif self.falando==True:
            print(f"{self.nome} não  pode falar pois está comendo")
        else:
            print(f"{self.nome} foi comer")
            self.comendo=True
    def dormi(self):
        if self.dormindo==True:
            print(f"{self.nome} está dormindo")
        elif self.comendo==True:
            print(f"{self.nome} não pode dormi pois está comendo")
        elif self.falando==True:
            print(f"{self.nome} não pode dormir pois está falando")
        else:
            print(f"{self.nome} foi  dormi")
            self.dormindo=True


class ContaBancaria():
    def __init__(self, numeroconta, nomeCliente, tipoConta ):
        self.numeroConta=numeroconta
        self.saldo=0
        self.statusConta=False
        self.nomeCliente=nomeCliente
        self.tipoConta=tipoConta
    def  ativarconta(self):
        if self.statusConta==False:
            self.statusConta=True
        else:
            print("Sua conta ja está ativada")

    












