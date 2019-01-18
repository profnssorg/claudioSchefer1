"""Programa 8_1.py 
Descrição: Escrever uma função que retorne o maior de dois números.
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

def máximo(a,b):
    if a>b:
        return a
    else:
        return b


# Saída de dados
print("máximo(a,b)) ==  -> obtido: %d" % máximo(a,b))
