"""Programa 6_10.py 
Descrição: Modificar o programa 6_9 de forma a pesquisar p e v em toda a lista e informando o usuário a posição onde foram encontrados
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis

L = []
p = int(0)
v = int(0)


# Entrada de dados


L = [15,7,27,39]
p = int(input("Digite o valor a procurar (p):"))
v = int(input("Digite o outro valor a procurar (v):"))


# Processamento

x = 0
achouP = -1 # -1 indica que ainda não foi encontrado o valor procurado
achouV = -1
primeiro = 0

while x < len(L):
     if L[x] == p:
         achouP = x
     if L[x] == v:
         achouV = x
     x += 1

# Saída de dados

if achouP != -1:
     print("p: %d encontrado na posição %d" %(p,achouP))
else:
     print("p: %d não encontrado" % p)

if achouV != -1:
     print("v: %d encontrado na posição %d" %(v,achouV))
else:
     print("v: %d não encontrado" % v)

