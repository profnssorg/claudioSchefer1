"""Programa 5_8.py 
Descrição:Programa que lê 2 números e imprime a multiplicação do 1º pelo 2º número usando + ou - para achar o resultado
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis
num1 = int(0)
num2 = int(0)


# Entrada de dados
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
x = 1  # contador
r = 0  # acumulador

# Processamento

while x <= num2:
    r = r + num1
    x = x + 1


# Saída de dados
print("%d * %d  = %d" % (num1,num2,r))
