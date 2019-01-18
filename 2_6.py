"""Programa 2_6.py 
Descrição: Modificar programa da listagem 2.11, de forma que ele calcule um aumento de 15% para um salário de R$ 750,00.
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis

salário = float()
aumento = float()


# Entrada de dados

salário = 750
aumento = 15


# Processamento

novo_salário = salário + (salário * aumento / 100)

# Saída de dados


print ("Novo salário: %s" % novo_salário)

