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
            print(f"{self.nome} não pode falar pois está comendo")
        else:
            self.falando = True
            print(f"{self.nome} começou a falar")


    def parar_falar(self):
        if self.falando==True:
            print(f"{self.nome} parou de falar")
            self.falando=False

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

    def parar_comer(self):
        if self.comendo==True:
            print(f"{self.nome} parou de comer")
            self.comendo=False


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

    def acordar(self):
        if self.dormindo==True:
            print(f"{self.nome} acordou")
            self.dormindo=False

class ContaBancaria():
    def __init__(self, NumeroConta, nomeCliente, tipoConta, saldo ):
        self.NumeroConta=NumeroConta
        self.saldo=0
        self.statusConta=False
        self.nomeCliente=nomeCliente
        self.tipoConta=tipoConta

    def ativar_conta(self):
        if self.statusConta==True:
            print("Sua conta já está ativada")
        else:
            self.statusConta=True


    def desativarconta(self):
         if self.statusConta==False:
                print("Conta ativada")
                self.statusConta=True


