class Pessoa:
    def __init__(self, nome, altura, raça):
        self.nome = nome
        self.altura = altura
        self.raça = raça
          
    def Cumprimentar(self):
        print("Oi! tudo bem com você? O meu nome é: " + self.nome)
        
    def PerguntarAltura(self):
        print("A sua altura é: " + self.altura + "?")
 
    def PerguntarRaça(self):
        print("A sua raça é: " + self.raça + "?")
        
pessoa1 = Pessoa("Ana", "1,60", "Parda")
pessoa2 = Pessoa("Pedro", "1,70", "Branco")
pessoa3 = Pessoa("Lorena", "1,80", "Negra")

print(pessoa1.Cumprimentar())
print(pessoa2.PerguntarAltura())
print(pessoa3.PerguntarRaça())




