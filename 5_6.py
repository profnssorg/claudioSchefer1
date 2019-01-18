"""Programa 5_6.py 
Descrição:Alterar o programa da listagem 5_9  para exibir os resultados no formato tabuada.
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis
x = int(0)
t = int(0)


# Entrada de dados
t = int(input("Digite qual tabuada deseja imprimir: "))

# Processamento
x = 1
while x <= 10:

# Saída de dados
	print("%d x %d = %d" %(t,x,t*x))
	x = x+1
