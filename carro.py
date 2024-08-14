#Criando a classe Carro

class Carro:
    def __init__(self, cor, modelo) :
        self.ligado = False 
        self.cor = cor 
        self.modelo = modelo 
        self.velocidade = 0

    def liga (self):
        if not self.ligado:
            self.ligado = True
            print (f"O {self.modelo} está ligado.")
        else:
            print (f"O {self.modelo} não está ligado.")

    def desliga (self):
        if self.ligado:
            self.ligado = False
            self.velocidade = 0
            print (f"O {self.modelo} está desligado.")
        else:
            print (f"O {self.modelo} já está desligado. ")
    
    def acelera (self, incremento):
        if self.ligado:
            self.velocidade += incremento
            print (f"O {self.modelo} aumentou sua velocidade para {self.velocidade}.")
        else:
            print (f"O {self.modelo} está desligado, por isso não pode acelerar. ")
    
    def desacelera (self, decremento):
        if self.ligado and self.velocidade > 0:
            self.velocidade -= decremento
            if self.velocidade < 0:
                self.velocidade = 0
            print (f"O {self.modelo} desacelerou para {self.velocidade} km\h. ")
        else:
            print (f"O {self.modelo} está desligado ou já está parado. ")


#Criando uma instância para meu carro
meu_carro = Carro (cor = "Rosa", modelo="BMW")

meu_carro.liga()
meu_carro.acelera(30)
meu_carro.acelera(10)

meu_carro.desacelera(30)
meu_carro.desacelera(10)
meu_carro.desliga()

meu_carro1 = Carro (cor = "Branco", modelo = "HB20")

meu_carro1.liga()
meu_carro1.acelera(15)
meu_carro1.acelera(2)

meu_carro1.desacelera(15)
meu_carro1.desacelera(1)
meu_carro1.desacelera(1)
meu_carro1.desliga()