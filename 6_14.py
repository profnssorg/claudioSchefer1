"""Programa 6_14.py 
Descrição:Rastrear o programa da listagem 6.44, mas com lista determinada e sequenciada.
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis
L = []
fim = int(0)

# Entrada de dados

L = [1,2,3,4,5]
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


# o fato de já termos sequenciamento na lista faz com que, após a primeira verificação
# de todos os elementos, seja interrompido o retorno para nova substituição. Como nenhum
# elemento é maior do que o elemento seguinte, o loop interno é interrompido pela condição "if not trocou"
  

