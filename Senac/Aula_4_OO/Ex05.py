# Crie uma classe ItemEstoque com os seguintes atributos: nome, quantidade e preco_unitario.
# Adicione os métodos:
# adicionar_estoque(quantidade) para aumentar o estoque.
# remover_estoque(quantidade) para reduzir o estoque,
# verificando a quantidade disponível.
# calcular_valor_total() que retorna o valor total do estoque.

class ItemEstoque:
    def __init__(self, nome, quantidade, preco_unitario):
        self.nome = nome
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario

    def exibir_estoque(self):
        print(f'Estoque disponível: {self.quantidade}')

    def adicionar_estoque(self, qntd):
        self.quantidade += qntd
        print(f'Adicionado {self.nome} com sucesso, quantidade atual em estoque: {self.quantidade}')

    def remover_estoque(self, quantidade):
        if (quantidade <= self.quantidade):
            self.quantidade -= quantidade
            print(f'{self.nome} Removido com sucesso, quantidade atual em estoque: {self.quantidade}')

        else:
            print(f'Quantidade insuficiente em estoque.')

    def calcular_valor(self):
        return self.quantidade * self.preco_unitario
    

item = ItemEstoque("Lapis", 50, 1.50)
item.adicionar_estoque(20)
item.remover_estoque(30)

print(f'Valor total em estoque: R$ {item.calcular_valor():.2f}')

