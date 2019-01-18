"""Programa 3_15.py 
Descrição: Escrever um programa que calcule a redução do tempo de vida de um fumante.
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis

qtdade_cigarros = int(0)
tempo = float()
tempo_perdido_por_cigarro = int(0)
dias_perdidos = float()



# Entrada de dados
qtdade_cigarros = int(input("Digite quantos cigarros fuma por dia: "))
tempo = float(input("Gigite quantos anos que vc fuma: "))
tempo_perdido_por_cigarro  = 10



# Processamento

dias_perdidos = qtdade_cigarros * tempo * 365 * 10 / 1440 



# Saída de dados

print("Dias perdidos: %5.2f " % dias_perdidos)
