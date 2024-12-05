# Dicionário
# Dicionários são usados ​​para armazenar valores de dados em pares chave:valor.
# Um dicionário é uma coleção ordenada*, mutável e que não permite duplicatas.

dicionario = {
  "Marca": "Ford",
  "Modelo": "Mustang",
  "Ano": 1964,
  "Marca2": "VW",
  "Modelo2": "Voyage",
  "Ano2": 2020
}
print('-'*50)
print(dicionario)

# Imprima o valor "marca" do dicionário:
print('-'*50)
print(dicionario["Marca2"])
print('-'*50)

# Duplicatas não permitidas
# Os dicionários não podem ter dois itens com a mesma chave

# O construtor dict()
#Também é possível usar o construtor dict() para criar um dicionário.

novo_dicionario = dict(nome = "John", idade = 36, cidade = "Nova Iguaçu")
print(novo_dicionario)
print('-'*50)

# Adicionando Itens
dicionario["Marca3"] = "Fiat"
print(dicionario)
print('-'*50)

# Removendo Itens
dicionario.pop("Marca")
print(dicionario)
print('-'*50)

# Como esvaziar um dicionario inteiro
dicionario.clear()
print(dicionario)