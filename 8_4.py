"""Programa 8_4.py 
Descrição: Escrever uma função que receba a base e a altura de um triângulo e retorne sua área (base x altura / 2)
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis

b = float()
a = float()

# Entrada de dados

b = float(input("Digite o valor da base do triângulo: "))
a = float(input("Digite a altura do triângulo: "))



# Processamento

def área_triângulo (b,a):
    return (b*a)/2



# Saída de dados
print("Área do triângulo cuja base é %s e a altura %s é: %s" %(b,a,área_triângulo (b,a)))
