# Exercício 4_3 "Programa que leia 3 números e imprima o maior e o menor"

# Declaração de variáveis
a = float(0) 
b = float(0) 
c = float(0)

# Entrada de dados / Inicialização (atribuição) de variáveis
a = float(input("Digite o primeiro valor: ")) 
b = float(input("Digite o segundo valor: ")) 
c = float(input("Digite o terceiro valor: "))

# Processamento
if b > a and b > c:
    maior = b 

if c > a and c > b:
    maior = c 
menor = a 

if b < c and b < a:
    menor = b 

if c < b and c <a:
    menor = c

# Saída de dados
print("O menor número digitado foi %5.2f: " % menor)
print("O maior número digitado foi %5.2f: " % maior)
