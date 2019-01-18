"""Programa 6_2.py 
Descrição:Fazer um programa para lêr duas listas e gerar uma terceira com os elementos das duas primeiras. 
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis

l = []



# Entrada de dados
l1 = []
l2 = []

# Processamento

while True:
    l = int(input("Digite valores para a primeira lista:"))
    if l==0:
        break
    l1.append(l) # append é usado para adicionar um elemento ao final de uma lista ou sequenciar uma lista

while True:
    l = int(input("Digite valores para a segunda lista:"))
    if l==0:
        break
    l2.append(l)

l3 = l1[:] # a terceira lista será uma cópia da primeira com adição da segunda lista
l3.extend(l2)

# Saída de dados

x=0 # primeiro elemento da lista tem indice 0

while x < len(l3): # a função len retorna o número de elementos da lista
    print("%d: %d" % (x, l3[x]))
    x=x+1
