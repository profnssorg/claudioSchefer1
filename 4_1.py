# Exercício 4_1 Analisar a listagem 4.2 e responder o que acontece quando os números são iguais

# Declaração de variáveis
a = int(0)
b = int(0)

## Inicialização (atribuição) de variáveis
a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))

# Processamento e saída de dados
if a>b:
    print("O Primeiro número é maior!!") 
if b>a:
    print("O Segundo número é maior!!") 
if a == b:
    print("Os números são iguais!!")

# quando os números forem iguais, não haverá retorno nenhum.
# Para resolver, podemos usar outra condição if, como realizado acima
