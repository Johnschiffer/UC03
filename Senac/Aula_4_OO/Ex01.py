# Crie uma classe chamada Pessoa com os atributos nome e idade.
# Adicione um método chamado exibir_informacoes que exibe o nome e a idade da pessoa.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir_informacoes(self):
        print(f"{self.nome}, {self.idade}")

    
nome1 = (input("Digite seu nome: "))
idade1 = (input("Digite sua idade: "))

pessoa1 = Pessoa(nome1, idade1)
pessoa1.exibir_informacoes()
