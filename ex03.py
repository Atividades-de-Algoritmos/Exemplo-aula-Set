#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 29/06/2022
#
# 3 – dado uma lista de valores, verifique quanto vezes cada elemento se repete (use conjuntos).
# l1 = ['a','b','b','a','c','c','c','d','d','e']

# criar a lista l1
l1 = ['a','b','b','a','c','c','c','d','d','e']
print(l1) #mostrar a lista l1

# cats l1 -> set
conjunto = set(l1) #criar um conjunto cats com os valores da lista l1 (set)
print(conjunto) #mostrar o conjunto cats com os valores

# processamento e saída de dados
for i in conjunto: #para cada valor do conjunto cats
  print(f"o valor {i} se repete {l1.count(i)} vezes") #mostrar o valor e a quantidade de vezes que ele se repete na lista l1
  print(f"o valor {i} se repete {l1.count(i):.2f} vezes") # para formatar a saída valor:.2f = 2 casas decimais (:.2f)
  

