"""Programa 5_10.py 
Descrição: Modificar o programa da listagem 5_10 para que aceite como resposta letras maiúsculas também
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis
pontos = int(0)
questão = int(0)

# Entrada de dados
pontos = 0
questão = 1

# Processamento
while questão <= 3:
     resposta = input("Resposta da questão %d: " % questão)
     if questão == 1 and resposta == "b" or resposta == "B":
         pontos = pontos + 1
     if questão == 2 and resposta == "a" or resposta == "A":
         pontos = pontos + 1
     if questão == 3 and resposta == "d" or resposta == "D":
         pontos = pontos + 1
     questão += 1

# Saída de dados
print("O aluno fez %d ponto(s)" % pontos)
