"""Programa 8_7.py 
Descrição:Definir uma função recursiva que calcule o maior divisor comum (MDC), 
entre dois números a e b, onde a >b.
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis

a = int(0)
b = int(0)


# Entrada de dados

a = int(input("Digite o valor de a (deve ser maior que b): "))
b = int(input("Digite o valor de b: "))


# Processamento

if a > b:

	def mdc(a,b):
		if b == 0:
		    return a
		return mdc(b, a % b)

else:
	print("Erro, a < b!!")

# Saída de dados


print("MDC a e b --> %d" % mdc(a,b))
