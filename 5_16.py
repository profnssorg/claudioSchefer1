"""Programa 5_16.py 
Descrição: Executar o programa da listagem 5.14 para os seguintes valores de entrada: 501,745,384,2,7 e 1.
tabalhar com notas de 50, 20, 10, 5, 1
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis

valor = int(0)
apagar = int(0)
cédulas = int(0)


# Entrada de dados

apagar = 0
cédulas = 0
atual = 50


# Processamento e saída de dados

valor = int(input("Digite o valor a pagar:"))
apagar = valor

while True:
     if atual <= apagar:
         apagar -= atual
         cédulas += 1
     else:
         print("%d cédula(s) de R$%d" % (cédulas, atual))
         if apagar == 0:
               break
         if atual == 50:
               atual = 20
         elif atual == 20:
               atual = 10
         elif atual == 10:
               atual = 5
         elif atual == 5:
               atual = 1
         cédulas = 0

# o programa processa os valores indicados sem nenhum problema
# para exercício 5_17, se digitarmos "0", o programa retorna 0 notas.
