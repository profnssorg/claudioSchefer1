"""Programa 5_7.py 
Descrição: Alterar o programa anterior de forma que o usuário informe também o final da tabuada 
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis
xi = int(0)
xf = int(0)
t = int(0)

# Entrada de dados
t = int(input("Digite qual tabuada deseja imprimir: "))
xi = int(input("Digite começo da tabuada:"))
xf = int(input("Digite o final da tabuada: "))

# Processamento
x = xi
while x <= xf:

# Saída de dados
	print("%d x %d = %d" %(t,x,t*x))
	x = x+1
