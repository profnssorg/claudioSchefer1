"""Descrição:Programa que leia os valores indicados e imprima a quantidade de notas necessárias para pagar este valor
tabalhar com notas de 50, 20, 10, 5, 1. Neste caso incluir a nota de 100 e para este caso, incluir valores decimais através de moedas de 0.01 / 0.02 / 0.05 / 0.10 e 0.50
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis

valor = float(0)
apagar = float(0)
cédulas = int(0)


# Entrada de dados

valor = float(input("Digite o valor a pagar:"))
cédulas = 0
atual = 100
apagar = valor


# Processamento e saída de dados

while True:
     if atual <= apagar:
         apagar -= atual
         cédulas += 1
     else:
         if atual >=1:
            print("%d cédula(s) de R$%d" % (cédulas, atual))
         else:
            print("%d moeda(s) de R$%5.2f" % (cédulas, atual))
         if apagar <0.01:
               break
         elif atual == 100:
            atual = 50
         elif atual == 50:
            atual = 20
         elif atual == 20:
            atual = 10
         elif atual == 10:
            atual = 5
         elif atual == 5:
            atual = 1
         elif atual == 1:
            atual = 0.50
         elif atual == 0.50:
            atual = 0.10
         elif atual == 0.10:
            atual = 0.05
         elif atual == 0.05:
            atual = 0.02
         elif atual == 0.02:
            atual = 0.01
         cédulas = 0
