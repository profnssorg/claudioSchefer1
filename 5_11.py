"""Programa 5_11.py 
Descrição: Escrever um programa que pergunte o depósito inicial e a taxa de juros de uma poupança.
Exibir os ganhos mensais para os 24 primeiros meses. Exiba o total de ganhos para o período
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis

depósito = float()
taxa = float()
n = int(0)
mês = int(0)
saldo = float()

# Entrada de dados
depósito = float(input("Digite o depósito inicial: "))
taxa = float(input("Digite a taxa de juros em %: "))
n = 24
mês = 1
saldo = depósito

# Processamento
while mês <= n:
	saldo = saldo + (saldo * (taxa / 100))

# Saída de dados
	print("Ganho do mês %d é de R$ %5.2f." % (mês, saldo))
	mês = mês + 1
print ("O ganho obtido com os juros foi de R$ %8.2f." % (saldo-depósito))

