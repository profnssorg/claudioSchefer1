"""Programa 5_21.py 
Descrição: Reescrever programa listagem 5_14 de forma a continuar executando até que o valor digitado seja 0
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis

valor = int(0)
cédulas = int(0)
atual = int(0)
saldo_a_pagar = int(0)

# Entrada de dados

cédulas = 0
atual = 50
saldo_a_pagar = valor


# Processamento e  Saída de dados

while True:
     valor = int(input("Digite o valor a pagar:"))
     if valor == 0:
       break
     cédulas = 0
     atual = 50
     saldo_a_pagar = valor

     while True:
     	if atual <= saldo_a_pagar:
        	saldo_a_pagar -= atual
        	cédulas += 1
     	else:
        	print("%d cédula(s) de R$%d" % (cédulas, atual))
        	if saldo_a_pagar == 0:
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



