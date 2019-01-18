"""Programa 6_16.py 
Descrição:Rastrear o programa da listagem 6.44, mas em ordem decrescente.
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis
L = []
x= int(0)
fim = int(0)
x = int(0) # é o índice da posição da lista, começando pela posição 0
e = int(0) # elementos da lista

# Entrada de dados

L = [1,2,3,4,5]
fim = 5 # quantidade de elementos da lista continua o mesmo

# Processamento

while fim > 1:
     trocou = False
     x = 0
     while x < (fim-1):
         if L[x] < L[x+1]: # aqui ocorre a comparação em si. A condição de verificação requer que o elemento posterior da lista seja menor que o anterior
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

