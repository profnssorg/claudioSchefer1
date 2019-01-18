"""Programa 8_3.py 
Descrição:Escrever uma função que receba o valor do lado (l) de um quadrado e 
# retorne sua área (A = lado²).
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis

l = float()
A = float()


# Entrada de dados

l = float(input("Digite o valor do lado l: "))



# Processamento

def área_quadrado (l):
    return l**2


# Saída de dados
print("Área do quadrado cujo lado mede %s : %s  " % (l, l**2))
