class Pessoa:
    nome = str()
    def __init__(self):
        self.set_nome("Digite o nome: ")
    
    def set_nome(self, msg):
        self.nome = input(msg)

    def get_nome(self):
        return self.nome

pessoas = list()

for c in range(0, 3, 1):
    pessoas.append(Pessoa())

for n in pessoas:
    print(n.get_nome())