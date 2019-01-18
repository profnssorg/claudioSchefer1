"""Programa 5_22.py
Descrição: Escrever um programa que exiba um menu com as opoes de + - / * e sair.
Imprimir a tabuada da operação escolhida.
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis

escolha = int(0)
n = int(0)
x = int(0)

# Entrada de dados

while True:
	print("""
Menu

1 - adição 
2 - subtração
3 - divisão
4 - multiplicação
5 - sair

""")

	escolha = int(input("Escolha uma opção: "))

# Processamento

	if escolha == 5:
        	break
	elif escolha >=1 and escolha <=4:
		n = int(input("Escolha uma Tabuada: "))
		x = 1
		while x <= 10:
			if escolha == 1:
				print("%d + %d = %d" % (n, x, n + x))
			elif escolha == 2:
                		print("%d - %d = %d" % (n, x, n - x))
			elif escolha == 3:
                		print("%d / %d = %5.4f" % (n, x, n / x))
			elif escolha == 4:
				print("%d x %d = %d" % (n, x, n * x))
			x=x+1

# Saída de dados
	else:
		print("Opção inválida!")
