class Pessoa():
    def __init__(self, nome, idade, peso):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.dormi=False
        self.falar=False
        self.comer=False
    def falar(self):
        print(f"{self.nome} começou a falar")
    def comer(self, comida):
        if self.comer==True:
            print(f"{self.nome} não pode comer, pois já está  comendo")
        print(f"Foi comer {comida}")
    def dormi(self):

        print(f"{self.nome} acabou de dormir.")
