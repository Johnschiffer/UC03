# Crie uma classe Livro com atributos titulo e autor.
# Sobrescreva o método especial __str__ para que, ao usar print em um objeto da classe,
# ele exiba o título e o autor do livro no formato: "Título: <titulo>, Autor: <autor>"

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Titulo: {self.name}, Autor: {self.age}"



nome1 = input("Digite o Titulo:")
autor1 = input("Digite o Autor: ")

nome_autor = Person(nome1,autor1)


print(nome_autor)
