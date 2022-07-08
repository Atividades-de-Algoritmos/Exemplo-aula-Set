#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 08/07/2022
#
# 2- ler um conjunto de 5 números e imprimir o menor e maior valor.

# Entrada e processamento de dados

c3 = set() # Criando um conjunto vazio para c3

for i in range(5): # For no range(5) significa que vai executar 5 vezes
  valor = int(input("Informe um valor: ")) # Solicitando um valor inteiro do usuário
  c3.add(valor) # Adicionando o valor ao conjunto c3

menor = min(c3) # Calculando o menor valor do conjunto c3 com min() e armazenando na variável menor
maior = max(c3) # Calculando o maior valor do conjunto c3 com max() e armazenando na variável maior

# Saída de dados

print(f"\nO menor é {menor} e o maior valor é {maior}") # Imprimindo o menor e maior valor do conjunto c3 com 5 valores
print('\nfim do programa')
