# Crie uma classe Estudante com atributos nome e notas (uma lista de notas). Adicione métodos para:
# Calcular a média das notas.
# Exibir uma mensagem dizendo se o estudante foi aprovado (média >= 6) ou reprovado.

class Estudante:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas
    
    def calcular_media(self):
        return sum(self.notas) / len(self.notas)
    
    def verificar_aprovacao(self):
        media = self.calcular_media()

        if media >= 6:
            print(f'{self.nome} aprovado com média: {media:.2f}')

        else:
            print(f'{self.nome} reprovado com média: {media}')



lista_notas = []

aluno = int(input("Digite a quantidade de aluno:"))
for alunos in range(aluno):
    nome = (input("Digite o nome: "))
    for x in range(4):
        nota = int(input(f"Digite a nota {x + 1}: "))
        lista_notas.append(nota)

estudantes = Estudante(nome, lista_notas)
estudantes.verificar_aprovacao()
