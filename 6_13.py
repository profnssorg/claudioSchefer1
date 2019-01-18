"""Programa 6_13.py 
Descrição:Fazer um programa que imprima a menor, a maior e a média das temperaturas apresentadas em uma lista.
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis

T = int(0)
x = int(0)
máxima = int(0)
mínima = int(0)
soma = int(0)


# Entrada de dados

T = [-10,-8, 0, 1, 2, 5, -2, -4]
x = 0
máxima = T[0]
mínima = T[0]
soma = 0


# Processamento

for e in T:
     if e > máxima:
         máxima = e
     if e < mínima:
         mínima = e
     soma = soma + e
     x +=1

# Saída de dados

print("Tempreatura máxima: %d ºC" % máxima)
print("Temperatura mínima: %d ºC" % mínima) 
print("Temperatura média: %d ºC" % (soma / x)) # poderíamos usar também o Len(T) como dividendo ao invés de x

