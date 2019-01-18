"""Programa 5_14.py 
Descrição:Escrever programa que leia números inteiros no teclado, até que o usuário digite 0.
Exibir a quantidade de números digitados, assim como a soma e a média aritmética.
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis

números = int(0)
soma = int(0)
quantidade = int(0)
média = float()

# Entrada de dados e 

soma = 0
quantidade = 0

# Processamento

while True:
    números = int(input("Digite um número inteiro: "))
    if números ==0:
        break;
    soma = soma + números
    quantidade = quantidade + 1
    média = soma / quantidade

# Saída de dados

print("Quantidade de números digitados:", quantidade)
print("Soma: ", soma)
print("Média: %10.2f" % (média))
