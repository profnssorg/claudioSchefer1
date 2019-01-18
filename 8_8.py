"""Programa 8_8.py 
Descrição:Usando a função mdc definida no exercício anterior, defina uma função para calcular 
o menor múltiplo comum (MMC) entre dois números.
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis

a = int(0)
b = int(0)


# Entrada de dados

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))


# Processamento

def mdc(a,b):
    if b == 0:
        return a
    return mdc(b, a % b)

def mmc(a,b):
    return abs(a*b) / mdc(a,b)


# Saída de dados


print("MMC a e b --> %d" % mmc(a,b))
