# Implemente uma classe chamada Produto com:
# Atributos: nome, preco e estoque.
# Um método chamado vender que reduz o estoque ao vender o produto, se houver unidades disponíveis.
# Um método chamado repor que aumenta o estoque ao receber novas unidades.

class Produto:
    def __init__(self, nome, preco=0, estoque=0):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def vender(self):
        
        if self.estoque > 0:
            vender = int(input("Digite a quantidade a vender: "))
            self.estoque -= vender
            print(f"Restam no estoque: {self.estoque}")
            if self.estoque <= 0:
                self.repor()
        else:
            print(f'Não há estoque disponivel')
            self.repor()
    
    def repor(self):
        qntd_repor = int(input("Quantidade a repor: "))
        self.estoque += qntd_repor
        print(f"Quantidade atual no estoque: {self.estoque}")

nome_produto1 = input("Digite o Nome do produto: ")
preco_produto1 = int(input("Digite o preço do produto: "))
estoque_produto1 = int(input("Quantidade em estoque: "))

produto1 = Produto(nome_produto1, preco_produto1, estoque_produto1)
produto1.vender()



