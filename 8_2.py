"""Programa 8_2.py 
Descrição: Escrever uma função que receba dois números e retorne True se o primeiro for múltiplo do segundo.
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis

a = int(0)
b = int(0)


# Entrada de dados

a = int(input("Digite a: "))
b = int(input("Digite b: "))


# Processamento
def múltiplo(a,b):
    return a % b == 0



# Saída de dados
print("múltiplo(a,b)  obtido: %s" % múltiplo(a,b))

