"""Programa 6_15.py 
Descrição:Rastrear o programa da listagem 6.44, com lista determinada e com valores repetidos.
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis
L = []
fim = int(0)

# Entrada de dados

L = [3,3,1,5,4]
fim = 5


# Processamento


while fim > 1:
     trocou = False
     x = 0
     while x < (fim-1):
         if L[x] > L[x+1]:
               trocou = True
               temp = L[x]
               L[x] = L[x+1]
               L[x+1] = temp
         x += 1
     if not trocou:
         break
     fim -= 1


# Saída de dados

for e in L:
     print(e)


# os números iguais / repetidos, entrarão no sequenciamento normal da série 

