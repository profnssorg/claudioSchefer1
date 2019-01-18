"""Programa 7_2.py 
Descrição: Escrever um programa que leia duas strings e que gere uma terceira com os caracteres em comum.
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis

s1 = ""
s2 = ""
s3 = ""

# Entrada de dados

s1 = input("Digite a primeira string: ")
s2 = input("Digite a segunda string: ")


# Processamento e Saída de dados 

for letra in s1:
    if letra in s2 and letra not in s3:
        s3+=letra

if s3 == "":
    print("Caracteres comuns não encontrados.")
else:
    print("Caracteres em comum: %s" % s3)





