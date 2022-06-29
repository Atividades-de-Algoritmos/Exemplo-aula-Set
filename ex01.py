#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 29/06/2022
#
# 1 - ler um conjunto de 4 número e em seguida mostra a média.

###          1         #####################################
c1 = set() # criar um conjunto vazio c1

#entrada de dados
valor = int(input("informe um valor: ")) #entrada de dados do valor
c1.add(valor) #adicionar o valor 1 ao conjunto c1

#saída de dados
print(c1) #mostrar o conjunto c1 com o valor


###          2         #####################################
c2 = set() # criar um conjunto vazio para c2

#entrada de dados
for i in range(4): #entrada de dados do conjunto c2 com 4 valores
  valor = int(input("informe um valor: ")) #entrada de dados do valor
  c2.add(valor) #adicionar o valor ao conjunto c2

#saída de dados
print(c2) #mostrar o conjunto c2 com os valores


###          3         #####################################
c3 = set() # criar um conjunto vazio para c3

#entrada de dados
for i in range(4): #entrada de dados do conjunto c3 com 4 valores
  valor = int(input("informe um valor: ")) #entrada de dados do valor do conjunto c3
  c3.add(valor) #adicionar o valor ao conjunto c3 com 4 valores
media = sum(c3) / len(c3) #calcular a média do conjunto c3 com 4 valores

menor = min(c3) #calcular o menor valor do conjunto c3 com 4 valores e armazenar na variável menor
maior = max(c3)

#saída de dados
print(f"o conjunto {c3}, a média dos valores é {media}") #mostrar o conjunto c3 com os valores e a média
print(f"o conjunto {c3}, a média dos valores é {media:.2f}") # para formatar a saída valor:.2f = 2 casas decimais
print(f"o menor é {menor} e maior valores é {maior}")