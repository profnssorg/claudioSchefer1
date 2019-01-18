"""Programa 6_17.py 
Descrição:Alterar a listagem 6.53 de forma a solicitar ao usuario o produto e a quantidade vendida.
Verificar se o nome do produto digitado existe no dicionário, e só então efetue a baixa do estoque.
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis

estoque = ""
quantidade = int(0)
preço = float ()
custo = float()


# Entrada de dados

estoque={ "tomate": [ 1000, 2.30],
          "alface": [   500, 0.45],
          "batata": [ 2001, 1.20],
          "feijão": [   100, 1.50] }
total = 0

print("Vendas:\n")

# Processamento


while True:
     produto = input("Nome do produto (fim para sair):")
     if produto == "fim":
        break
     if produto in estoque:
        quantidade = int(input("Quantidade:"))
        if quantidade <= estoque[produto][0]:
            preço = estoque[produto][1]
            custo = preço * quantidade
            print("%10s: %3d x %6.2f = %6.2f" % (produto, quantidade,preço,custo))
            estoque[produto][0] -= quantidade
            total += custo
        else:
            print("Quantidade solicitada não disponível")
     else:
        print("Nome de produto inválido")


# Saída de dados

print(" Custo total: %10.2f\n" % total)
print("Estoque:\n")

for chave, dados in estoque.items():
     print("Descrição: ", chave)
     print("Quantidade: ", dados[0])
     print("Preço: %6.2f\n" % dados[1])
