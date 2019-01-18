"""Programa 5_25.py 
Descrição:Programa que calcule a raiz quadrada de um número
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis
n = float()
b = int(0)



# Entrada de dados

n=float(input("Digite um número para encontrar a sua raiz quadrada: "))
b=2


# Processamento

while abs(n-(b*b))>0.0001:
    p=(b+(n/b))/2
    b=p


# Saída de dados

print ("A raiz quadrada de %d é aproximadamente %8.4f" % (n, p))
