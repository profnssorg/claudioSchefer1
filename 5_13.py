"""Programa 5_13.py 
Descrição: Escrever um programa que pergunte o valor inicial de uma dívida e o juro mensal.
Pergunte também o valor mensal que será pago. Imprimir o número de meses para que a dívida seja paga.
Exibir o total pago e o total de juros pago.
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis

di = float()
taxa = float()
am = float()
mês = int(0)


# Entrada de dados

di = float(input("Digite o  valor da dívida inicial: "))
taxa = float(input("Digite a taxa de juros: "))
am = float(input("Digite valor da amortização mensal: "))
mês = 1
saldo = di


# Processamento

if (di * (taxa/100) > am):
    print("Sua dívida nunca será paga pois os juros são superiores ao pagto mensal.")

else:
    saldo = di
    juros_pago = 0

    while saldo > am:
        juros = saldo * taxa / 100
        saldo = saldo + juros - am
        juros_pago = juros_pago + juros

# Saída de dados

        print("Saldo da dívida no mês %d é de R$ %6.2f." % (mês, saldo))
        mês = mês + 1

    print("Para pagar uma dívida de R$ %8.2f, a %5.2f %% de juros, você precisará de %d meses." %(di,taxa, mês-1)) 
    print("Total de juros pago será de  R$ %8.2f." % (juros_pago))
