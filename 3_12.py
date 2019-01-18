"""Programa 3_12.py 
Descrição: Escrever um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada.
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis




# Entrada de dados

distância = int(input("Digite a distância a ser percorrida em Km: " ))

velocidade_média = float(input("Digite a velocidade média esperada em Km / hora: " ))


# Processamento

tempo_de_viagem = distância / velocidade_média


# Saída de dados

print("O tempo de viagem é de %5.2f horas" % tempo_de_viagem)
