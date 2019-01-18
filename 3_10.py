"""Programa 3_10.py 
Descrição:Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem de aumento. Exibir o valor do aumento e do novo salário. 
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis




# Entrada de dados

salário_atual = float(input("Digite o salário atual: "))
aumento = float(input("Digite o valor percentual de aumento: "))



# Processamento

valor_do_aumento = salário_atual * (aumento/100)

salário_final = salário_atual + valor_do_aumento


# Saída de dados

print("Aumento será de %5.2f e o novo  salário será %7.2f" %(valor_do_aumento, salário_final))
