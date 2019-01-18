"""Programa x_x.py 
Descrição:
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
p = int(input("Digite o valor (p) a procurar:"))
v = int(input("Digite o outro valor (v) a procurar:"))


# Processamento

x = 0
achouP = False
achouV = False
primeiro = 0

while x < len(L):
     if L[x] == p:
         achouP = True
         if not achouV:
            primeiro = 1
     if L[x] == v:
         achouV = True
         if not achouP:
            primeiro = 2
     x += 1

# Saída de dados

if achouP:
     print("p: %d encontrado" % p)
else:
     print("p: %d não encontrado" % p)
if achouV:
     print("v: %d encontrado" % v)
else:
     print("v: %d não encontrado" % v)
if primeiro == 1:
    print("p foi achado antes de v")
elif primeiro == 2:
    print("v foi achado antes de p")

