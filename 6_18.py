"""Programa 6_18.py 
Descrição: Escrever um programa que gere um dicionário, onde cada chave seja um caracter e seu valor o número de xs em que a letra aparece
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis

d = {}
frase = ""

# Entrada de dados

frase = input("Digite uma frase para contar as letras:")


# Processamento

d = {}
for letra in frase:
    if letra in d:
        d[letra] = d[letra] + 1
    else:
        d[letra] = 1



# Saída de dados

print(d)
