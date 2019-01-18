"""Programa 6_11.py 
Descrição:Modificar programa da listagem 6.15 usando for.
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis

L = []
n = int(0)

# Entrada de dados

n


# Processamento


while True:   # este  while não pode ser alterado para for pq não sabemos o número de repetições.

     n = int(input("Digite um número (0 sai):"))
     if n == 0:
         break
     L.append(n)


# Saída de dados

for e in L:
     print(e)


