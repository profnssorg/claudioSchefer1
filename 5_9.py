"""Programa 5_9.py 
Descrição: Escrever programa que leia 2 números, imprima a divisão inteira do 1º pelo 2º e o resto. Utilizar apenas + e -
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis


num1 = int(0)
num2 = int(0)


# Entrada de dados

num1 = int(input("Digite o primeiro número: ")) # dividendo
num2 = int(input("Digite o segundo número: ")) # divisor
quociente = 0
x = num1

# Processamento
while x >= num2:
	x = x - num2
	quociente = quociente + 1
resto = x

quociente = num1 / num2

# Saída de dados
print("%d / %d = %d (quociente) %d (resto)" % (num1, num2, quociente, resto))
