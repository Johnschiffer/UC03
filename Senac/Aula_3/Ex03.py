alunos = []


def adicionar_aluno(nome):
    alunos.append(nome)
    print(f"Aluno {nome} adicionado!")


def remover_aluno(nome):
    if nome in alunos:
        alunos.remove(nome)
        print(f"Aluno {nome} removido!")
        
    else:
        print(f"Aluno {nome} não encontrado.")


def listar_alunos():
    print("Lista de Alunos:")
    for aluno in alunos:
        print(aluno)


while True:
    op = input('Operação: 1 - inserir / 2 - remover / 3 - listar / outro pra sair ')
    if op == '1':
        adicionar_aluno(input('Informe o nome: '))
    elif op == '2':
        remover_aluno(input('Informe o nome: '))
    elif op == '3':
        listar_alunos()
    else:
        break