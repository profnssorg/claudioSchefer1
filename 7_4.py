"""Programa 7_4.py 
Descrição: Escrever um programa que leia uma string e imprima quantas vezes cada caracter aparece.
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis

s = ""
d = {}


# Entrada de dados

s = input("Digite a string:") 
d = {}

# Processamento

for letra in s:
    if letra in d:
        d[letra] = d[letra] + 1
    else:
        d[letra] = 1

for chave in d:

# Saída de dados

    print(" %s : %dx" % (chave, d [chave]))
