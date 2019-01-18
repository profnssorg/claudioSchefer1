"""Programa 3_8.py 
Descrição: Escrever um programa que leia em metros e exiba o valor em milímitros.
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis

metros = float()
milímetros = float()

# Entrada de dados


metros = float(input("Digite o valor em métros: "))

# Processamento

milímetros = metros * 1000


# Saída de dados

print("%20.3f metros equivalem a %10.3f milímetros." % (metros, milímetros))

