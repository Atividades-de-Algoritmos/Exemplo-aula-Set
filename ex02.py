#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 29/06/2022
#
# 2- ler um conjunto de 5 números e imprimir o menor e maior valor.


###          1         #####################################
c3 = set() # criar um conjunto vazio para c3

#entrada de dados
for i in range(5): #entrada de dados do conjunto c3 com 5 valores
  valor = int(input("informe um valor: ")) #entrada de dados do valor do conjunto c3
  c3.add(valor) #adicionar o valor ao conjunto c3 com 4 valores
media = sum(c3) / len(c3) #calcular a média do conjunto c3 com 5 valores

menor = min(c3) #calcular o menor valor do conjunto c3 com 5 valores e armazenar na variável menor
maior = max(c3) #calcular o maior valor do conjunto c3 com 5 valores e armazenar na variável maior

#saída de dados
print(f"o conjunto {c3}, a média dos valores é {media}") #mostrar o conjunto c3 com os valores e a média
print(f"o conjunto {c3}, a média dos valores é {media:.2f}") # para formatar a saída valor:.2f = 2 casas decimais
print(f"o menor é {menor} e maior valores é {maior}") #mostrar o menor e maior valor do conjunto c3 com 5 valores