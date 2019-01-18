"""Descrição:Programa que leia os valores indicados e imprima a quantidade de notas necessárias para pagar este valor
tabalhar com notas de 50, 20, 10, 5, 1. Neste caso incluir a nota de 100
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis

valor = int(0)
apagar = int(0)
cédulas = int(0)


# Entrada de dados

valor = int(input("Digite o valor a pagar:"))
cédulas = 0
atual = 100
apagar = valor


# Processamento e saída de dados


while True:
     if atual <= apagar:
         apagar -= atual
         cédulas += 1
     else:
         print("%d cédula(s) de R$%d" % (cédulas, atual))
         if apagar == 0:
               break
         if atual ==100:
               atual = 50
         if atual == 50:
               atual = 20
         elif atual == 20:
               atual = 10
         elif atual == 10:
               atual = 5
         elif atual == 5:
               atual = 1
         cédulas = 0

