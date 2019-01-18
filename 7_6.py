"""Programa 7_6.py 
Descrição: Escrever um programa que leia três strings e imprima o resultado da substituição
na primeira, dos caracteres da segunda pelos da terceira.
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis

s1 = ""
s2 = ""
s3 = ""
s4 = "" # o resultado da substituição

# Entrada de dados

s1 = input("Digite a primeira string: ")
s2 = input("Digite a segunda string: ")
s3 = input("Digite a terceira string: ")

# Processamento e Saída de dados 

if len(s2) == len(s3):
    s4 = ""
    for letra in s1:
        posição = s2.find(letra)
        if posição != -1:
            s4 += s3[posição]
        else:
            s4 += letra

    if s4 == "":
        print("Todos os caracteres foram removidos.")
    else:
        print("Os caracteres %s foram substituidos por %s em %s, gerando: %s" % (s2, s3, s1, s4))
else:
    print("ERRO: A segunda e a terceira string devem ter o mesmo tamanho.")



