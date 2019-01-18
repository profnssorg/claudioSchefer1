"""Programa 8_12.py 
Descrição: Escrever uma função que receba uma string e uma lista.
A função deve comparar a string passada com os elementos da lista, também passada como parâmetro.
Retronar verdadeiro se a string for encontrada dentro da lista, e falso em caso contrário.
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis

s = ""
l = []

# Entrada de dados


L = ["AB", "CD", "EF"]

# Processamento

def procura_string(s,lista):
    return s in lista


# Saída de dados

print(procura_string("AB", L))
print(procura_string("CD", L))
print(procura_string("XYZ", L))
