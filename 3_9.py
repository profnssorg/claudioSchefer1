"""Programa 3_9.py 
Descrição: Escrever um programa que leia a quantidade de dias, horas, minutos e segundos do usuário e calcule o total em segundos
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis




# Entrada de dados
d = int(input("Digite a quantidade de dias: "))
h = int(input("Digite a quantidade de horas: "))
m = int(input("Digite a quantidade de minutos: "))
s = int(input("Digite a quantidade de segundos: "))


# Processamento

tt_em_segundos = d * 24 * 60 * 60 + h * 60 * 60 + m *60 + s


# Saída de dados


print("O total em segundos é igual a: %5d segundos. " % tt_em_segundos)
