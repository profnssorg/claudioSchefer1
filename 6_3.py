"""Programa 6_3.py 
Descrição:Fazer um programa que percorra duas listas e gere uma terceira sem elementos repetidos
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis

primeira = []
segunda = []
terceira = []
duas_listas = []



# Entrada de dados e  Processamento



while True:
    e = int(input("Digite um valor para a primeira lista (0 para terminar):"))
    if e==0:
        break
    primeira.append(e)

while True:
    e = int(input("Digite um valor para a segunda lista (0 para terminar):"))
    if e==0:
        break
    segunda.append(e)

terceira = [] # Aqui vamos criar uma outra lista, com os elementos da primeira e da segunda. 

duas_listas = primeira[:]
duas_listas.extend(segunda)

x=0
while x < len(duas_listas):
    y = 0
    while y < len(terceira):
        if duas_listas[x] == terceira[y]:
            break;
        y=y+1
    if y == len(terceira):
        terceira.append(duas_listas[x])
    x=x+1


# Saída de dados

x=0
while x < len(terceira):
    print("%d: %d" % (x, terceira[x]))
    x=x+1
