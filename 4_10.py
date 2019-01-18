# Exercício 4_10 "Programa para calcular o preço a pagar pelo fornecimento de energia de acordo com a quantidade e tipo de instalação.


# Declaração de variáveis
qtdade = float()
preço = float()

# Inicialização (atribuição) de variáveis
qtdade = float(input("Informe 0 consumo em KWh: "))
tipo = input("Informe tipo de instalação(R,I ou C): ")

# Processamento
if tipo == "R":
    if qtdade <= 500:
        preço == 0.40
    else:
        preço = 0.65
elif tipo == "I":
    if qtdade <= 5000:
        preço = 0.55
    else:
        preço = 0.60
elif tipo == "C":
    if qtdade <= 1000:
        preço = 0.55
    else:
        preço = 0.60
else:
	preço = 0
	print("Erro! Tipo desconhecido!")

custo = qtdade * preço

# Saída de dados
print("Valor a pagar: R$ %7.2f" % custo)

