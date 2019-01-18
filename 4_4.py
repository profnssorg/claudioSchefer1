# Exercício 4_4 Programa que pergunte o salário e calcule o valor do aumento

# Declaração de variáveis
salario = float()
aumento = float()

# Inicialização (atribuição) de variáveis
salario = float(input("Digite seu salário: "))


# Processamento
if salario >= 1250:
    aumento = salario * 0.1

if salario < 1250:
    aumento = salario * 0.15
    
# Saída de dados 
print("aumento será de: R$ %7.2f" % aumento)
