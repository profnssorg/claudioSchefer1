"""Programa 5_15.py 
Descrição:Programa para controlar máquina registradora.Usuário deve digitar o código do produto e a quantidade comprada.
Exibir o total gasto depois que usuário digitar 0.
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis

código = int(0)
quantidade = float()
total_a_pagar = float()
preço = float()

# Entrada de dados e Processamento
total_a_pagar = 0
preço = 0

while True:
    código = int(input("Código da mercadoria (0 para sair):"))
    preço = 0

    if código == 0:
        break;
    elif código == 1:
        preço = 0.50
    elif código == 2:
        preço = 1.00
    elif código == 3:
        preço = 4.00
    elif código == 5:
        preço = 7.00
    elif código == 9:
        preço = 8.00
    else:
        print("Código inválido!")

    if preço != 0:
        quantidade = int(input("Quantidade:"))
        total_a_pagar = total_a_pagar + (preço * quantidade)


# Saída de dados
print("Total a pagar R$%6.2f" % total_a_pagar)

