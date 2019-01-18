"""Programa 8_6.py 
Descrição:Reescrever programa da listagem 8.8 de forma a utilizar for em vez de while
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis

L = []


# Entrada de dados

L = [1,7,2,9,15]

# Processamento

def soma(L):

     total = 0
     x = 0

     for e in L:
         total += L[x]
         x+=1

     return total


# Saída de dados


print(soma(L))
print(soma([7,9,12,3,100,20,4]))
