"""Programa 8_13.py 
Descrição: Alterar o programa da listagem 8.37 de forma que o s=usuário tenha 03 chances de acertar
o número. O programa deve terminar após as 03 tentativas.
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis

n = int(0)
x = int(0)
tentativas = int(0)



# Entrada de dados

import random
n = random.randint(1, 10)
tentativas = 0

# Processamento e saída de dados

while tentativas < 3:
    x = int(input("Escolha um número entre 1 e 10:"))
    if x == n:
        print("Você acertou!")
    else:
        print("Você errou.")
    tentativas += 1



