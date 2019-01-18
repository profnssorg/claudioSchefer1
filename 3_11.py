"""Programa 3_11.py 
Descrição: Fazer um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exibir o valor do desconto e o preço a pagar. 
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis




# Entrada de dados

preço = float(input("Digite o valor da mercadoria: "))

desconto = float(input("Digite o percentual de desconto: "))


# Processamento

valor_desconto = preço*(desconto/100)

valor_a_pagar = preço - (preço*(desconto/100))




# Saída de dados

print("Desconto obtido: %5.2f e valor final a pagar: %5.2f " %(valor_desconto, valor_a_pagar))
