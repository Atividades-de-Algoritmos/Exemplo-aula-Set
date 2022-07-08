#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 08/07/2022
#
# 3 – dado uma lista de valores, verifique quanto vezes cada elemento se repete (use conjuntos).
# l1 = ['a','b','b','a','c','c','c','d','d','e']


# Entrada de dados

l1 = ['a','b','b','a','c','c','c','d','d','e'] # Criando a lista l1
print(f'lista l1 -> {l1}\n') # Imprimindo a lista l1

# Cast l1 -> set
conjunto = set(l1) # Criando um conjunto com os valores da lista l1 (set)
print(f'Set l1 -> {conjunto}\n') # Imprimindo o conjunto com os valores

# Processamento e saída de dados

for i in conjunto: # Para cada valor do conjunto
  print(f"O valor {i} se repete {l1.count(i)} vezes") # Mostrando o valor e a quantidade de vezes que ele se repete na lista l1
  # print(f"O valor {i} se repete {l1.count(i):.2f} vezes") # Para formatar a saída valor:.2f = 2 casas decimais (:.2f)

print('\nfim do programa')
