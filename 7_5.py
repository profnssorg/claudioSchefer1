"""Programa 7_5.py 
Descrição: Escrever um programa que leia duas strings e  gere uma terceira na qual os
 caracteres da segunda foram retirados da primeira.
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
    if letra not in s2:
        s3 += letra

if s3 == "":
    print("Todos os caracteres foram removidos.")
else:
    print("Os caracteres %s foram removidos de %s, gerando: %s" %(s2,s1,s3))




