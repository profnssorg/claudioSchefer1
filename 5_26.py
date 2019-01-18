"""Programa 5_26.py 
Descrição: Escrever um programa que calcule o resto da divisão de 2 números, utilizando apenas soma e subtração para calcular o resultado
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis

dividendo = int(0)
divisor = int(0)
quociente = int(0)
resto = float(0)

# Entrada de dados

dividendo = int(input("Dividendo:"))
divisor = int(input("Divisor:"))
quociente = 0

# Processamento

x = dividendo
while x >= divisor:
    x = x - divisor
    quociente = quociente + 1
resto = x

# Saída de dados
print("O resto de %d / %d é %d" % (dividendo,divisor,resto))
