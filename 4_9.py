# Exercício 4_9 "Programa para aprovar empréstimo bancário"


# Declaração de variáveis
valor = float()
salário = float()
parcelas = int(0)
prestação = int(0)


# Inicialização (atribuição) de variáveis
valor = float(input("Informe o valor da casa a ser financiada: "))
salário = float(input("Informe o valor do seu salário: "))
parcelas = int(input("Informe a quantidade de meses do financiamento: ")) 


# Processamento e Saída de dados
prestação = valor / parcelas
if prestação <= 0.3 * salário:
    print("Empréstimo liberado. Valor da prestação: R$ %7.2f" % prestação)
else:
    print("Empréstimo não liberado, pois valor da prestação é maior que 30% do salário")

