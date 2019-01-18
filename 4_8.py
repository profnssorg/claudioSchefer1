
# Exercício 4_8 "Programa para ler dois números e perguntar qual operação deseja realizar:  + / - / * ou /. Exibir o resultado da operação"


# Declaração de variáveis
num1 = float()
num2 = float()


# Inicialização (atribuição) de variáveis
num1 = float(input("Informe o primeiro valor: "))
num2 = float(input("Informe o segundo valor: "))
operacao = input("Qual operação você deseja realizar(+,-,* ou /): ")

# Processamento
if operacao == "+":
	resultado = num1 + num2
elif operacao == "-":
	resultado = num1 - num2
elif operacao == "*":
	resultado = num1*num2
elif operacao == "/":
	resultado = num1/num2
else:
	print("Operação inválida!")

# Saída de dados
print("Resultado:", resultado)

