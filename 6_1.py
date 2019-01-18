"""Programa 6_1.py 
Descrição:"Modificar programa da listagem 6.6 para ler 7 ao invés de 5 notas"
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis

notas = float()
soma = float()

# Entrada de dados
notas = [0,0,0,0,0,0,0]  # lista onde 07 notas devem ser lidas / inseridas

# Processamento e saída de dados

soma = 0
x = 0

while x < 7:
    notas[x] = float(input("Nota %d:" % x))
    soma += notas[x]
    x += 1
x = 0
while x < 7:
    print("Nota %d: %6.2f" % (x, notas[x]))
    x += 1

print("Média: %5.2f" % (soma/x))
