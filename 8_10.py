"""Programa 8_10.py 
Descrição: Reescrever a função para cálculo da sequência de Fibonacci, sem utilizar recursão.
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis

n = int(0)

# Entrada de dados

n = int(input("Digite o valor de n: "))


# Processamento

def fibonacci(n):
    fibonacci = 1
    while n > 1:
        fibonacci *= n
        n-=1
    return fibonacci

for x in range(15):
    print("fibonacci(%d) = %d" % (x,fibonacci(x)))



# Saída de dados
