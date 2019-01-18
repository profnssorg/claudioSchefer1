"""Programa 4_2.py 
Descrição: Pergunta a velocidade do carro e informa o valor da multa caso ele esteja acima de 80 km/h,
 sendo o valor cobrado de R$ 5,00 / km.
Autor:Cláudio Schefer
Data: 29/11/2018
Versão: 001
"""

# Entrada de dados
velocidade = float()
multa = float()

## Declaração de variáveis


## Inicialização (atribuição) de variáveis

velocidade = float(input("Digite a velocidade do seu carro em Km/h: "))
multa = float()

# Processamento e saída de dados

if velocidade > 80:
    multa = (velocidade - 80) * 5
    print("Você foi multado em R$ %7.2f!" % multa)
if velocidade <= 80:
    print("Sua velocidade está ok, boa viagem!")

