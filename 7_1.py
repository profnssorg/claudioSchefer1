"""Programa 7_1.py 
Descrição: Escrever um programa que leia duas strings e verifique se a segunda ocorre dentro da primeira
Imprimir a posição de início
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis

s1 = ""
s2 = ""

# Entrada de dados

s1 = input("Digite a primeira string: ")
s2 = input("Digite a segunda string: ")


# Processamento e Saída de dados


posição = s1.find(s2)

if posição == -1:
    print("'%s' não encontrada em '%s'" % (s2, s1))
else:
    print("%s encontrada na posição %d de %s"  % (s2, posição, s1 ))

