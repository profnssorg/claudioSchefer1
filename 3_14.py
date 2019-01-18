"""Programa 3_14.py 
Descrição:Escrever um programa que pergunte kms percorrido por um carro alugado, quantidade de dias alugado. Exibir o preço a pagar
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis

dist_percorrida = int(0)
qtdade_dias = int(0)
valor_a_pagar = float()


# Entrada de dados

dist_percorrida = int(input("Digite a distância percorrida com o carro: "))
qtdade_dias = int(input("Digite a quantidade de dias que ficou com o carro: "))
preço_por_dia = 60
preço_por_km = 0.15

# Processamento

valor_a_pagar = dist_percorrida * 0.15 + qtdade_dias * 60



# Saída de dados

print("Valor_a_pagar: R$ %7.2f " % valor_a_pagar)
