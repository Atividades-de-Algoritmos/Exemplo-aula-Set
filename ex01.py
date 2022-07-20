#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 20/08/2022
#
# 1 - ler um conjunto de 4 números e em seguida mostrar a média.

# Versão 1.0 do código, solicita apenas um valor;

# ------------------------------------------------- #

# Entrada de dados

c1 = set() # Criando um conjunto vazio c1
valor = int(input("informe um valor: ")) # Solicita um valor inteiro do user

# Processamento e saída de dados

c1.add(valor) # Adicionando o valor 1 ao conjunto c1
print(c1) # Imprimindo o conjunto c1 com o valor

# ------------------------------------------------- #

# Versão 2.0 do código, solicitando os 4 valores;

# -------------------------------------------------- #

# Entrada e processamento de dados

c2 = set() # Criando um conjunto vazio para c2

for i in range(4): # For com o tamanho 4 irá executar 4 vezes.
   valor = int(input("informe um valor: ")) # Solicita um valor inteiro do user
   c2.add(valor) # Adiciona o valor ao conjunto c2

# Saída de dados

print(c2) # Imprimindo o conjunto c2 com os valores.

# --------------------------------------------------- #

# Versão 3.0 do código que solicita os 4 valores e ainda mostra a média

# ---------------------------------------------------- #

# Entrada de dados

c3 = set() # Criando um conjunto vazio para c3

for i in range(4): # For com range(4) significa que irá rodar 4 vezes
  valor = int(input("Informe um valor: ")) # Solicitando um valor inteiro do user
  c3.add(valor) # Adicionando valor solicitado ao conjunto c3

# Processamento de dados

media = sum(c3) / len(c3) # Calculando a média usando o sum() função que soma todos os elementos do conjunto, em seguida dividindo por len() que conta quantos elementos existem dentro do conjunto.

# Saída de dados

print(f"\nO conjunto {c3}, a média dos valores é {media}") # Imprimindo o conjunto c3 com os valores e a média
print(f"O conjunto {c3}, a média dos valores é {media:.2f}") # Para formatar a saída valor:.2f = 2 casas decimais
print('\nfim do programa')

# ----------------------------------------------------- #
