"""Programa 5_12.py 
Descrição: Alterar o programa 5_11 de forma a perguntar também o valor mensal depositado.
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis

depósito = float()
depósito_mensal = float()
taxa = float()
n = int(0)
mês = int(0)
saldo = float()

# Entrada de dados

depósito = float(input("Digite o depósito inicial: "))
depósito_mensal = float(input("Digite o valor depositado mensalmente "))
taxa = float(input("Digite a taxa de juros em %: "))
n = 24
mês = 1
saldo = depósito
saldo = depósito + depósito_mensal

# Processamento

while mês <= n:
	saldo = saldo + (saldo * (taxa / 100)) + depósito_mensal

# Saída de dados

	print("Saldo do mês %d é de R$ %5.2f." % (mês, saldo))
	mês = mês + 1
print ("O ganho obtido com os juros foi de R$ %8.2f." % (saldo-depósito))

