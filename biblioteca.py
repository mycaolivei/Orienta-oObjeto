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

class Animal():
    def  __init__(self, nome, cor):
        self.nome=nome
        self.cor=cor

    def comer(self):
        print(f"O {self.nome} foi comer...")

class Gato(Animal):
    def __init__(self, nome,  cor):
        super().__init__(nome,cor)

    def miar(self):
        print(f"O {self.nome} foi miando")

class Vaca(Animal):
    def __init__(self,  nome, cor):
        super().__init__(nome,cor)

    def mugir(self):
        print(f"A {self.nome} faz muuuuuuuuuu")

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def latir(self):
        print(f"O {self.nome} faz auauauauauau")

class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome,cor)

    def grunindo(self):
        print(f"O {self.nome} faz iiii iiii iiii ")

class Ingresso():
    def __init__(self, valor):
        self.valor=valor

    def imprimeValor(self):
        print(f"O ingresso custa {self.valor}")


class VIP(Ingresso):
    def __init__(self, valor):
        super().__init__(valor)
        self.valor2=valor*1.5

    def imprimeValor(self):
       print(f" Seu ingresso vip  custou R${self.valor2}")


class Forma():
    def __init__(self):
        self.area=0
        self.perimetro=0

class Retangulo(Forma):
     def __init__(self):
         super().__init__()

     def calcularArea(self, base, altura):
            self.area=base*altura
            print(f"O calculo da area do triangulo é {self.area}")

     def calcularperimmetro(self, base, altura):
         self.perimetro= 2*(base+altura)
         print(f"O perimetro do retangulo é {self.perimetro}")

class Triangulo(Forma):
      def __init__(self, altura):
        super().__init__()

          




class Atleta():
    def __init__(self):
        self.aposentado=False
        self.peso=0
        self.aquecer=False

    def aposentar(self):
        if self.aposentado==True:
         print("Ele já está aposentado")
         return

        elif self.aquecer==True:
         print("Ele não pode aposentar, está aquecendo")
         self.aquecer=True

        else:
         print("Ele está aposentado")
         self.aposentado=True

    def aquecido(self):
       if  self.aquecer==True:
           print("Ele já está aquecendo")
           return

       elif self.aposentado==True:
           print("Ele não pode aquecer, está aposentado")
       else:
        print("Ele está aquecendo")

        self.aquecer=True


class Corredor(Atleta):
    def __int__(self):
        super().__init__()

    def correr(self):
        if self.aquecer==True:
            print("Ele já está aquecido e pode correr")
            return
        elif self.aposentado==True:
            print("Ele está aposentado, não pode correr")
        else:
          print("Ele está correndo")
        self.aquecer=True


class Nadador(Atleta):
    def __init__(self):
        super().__init__()

    def nadar(self):
        if self.aquecer==True:
            print("Ele está aquecido, pode nadar")

        elif self.aposentado==True:
            print("Ele não pode nadar, está aposentado")

        else:
            print("Ele já está nadando")
        self.aquecer=True

class Ciclista(Atleta):
    def __int__(self):
        super().__init__()
        if self.aquecer==True:
            print("Ele está aquecido e pronto pra pedalar")
            return
        elif self.aposentado==True:
            print("Ele está aposentado, não pode pedalar")

        else:
            print("Ele já está pedalando")

class Triatleta(Corredor,Nadador,Ciclista):
    def __init__(self):
        super().__init__()


