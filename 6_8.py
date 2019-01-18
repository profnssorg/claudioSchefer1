"""Programa 6_8.py 
Descrição:Modificar listagem 6_23 de modo a realizar a mesma tarefa, mas sem utilizar a variável achou
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis
L = []
p = int(0)


# Entrada de dados

L = [15,7,27,39]
p = int(input("Digite o valor a procurar:"))


# Processamento e Saída de dados

x = 0
while x < len(L):
     if L[x] == p:
          break
     x += 1
if x < len(L):
     print("%d achado na posição %d" % (p,x))
else:
     print("%d não encontrado" % p)
