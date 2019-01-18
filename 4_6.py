# Exercício 4_6 "Perguntar a distãncia a percorrer e calcular  valor a ser pago"

# Declaração de variáveis
distância = float()


# Inicialização (atribuição) de variáveis
distância = float(input("Digite a distância a ser percorrida em Km: "))

# Processamento
if distância <= 200:
    valor_da_passagem = distância * 0.5
else:
    valor_da_passagem = distância * 0.45

# Saída de dados
print("O valor da sua passagem é: R$ %7.2f" % valor_da_passagem)
