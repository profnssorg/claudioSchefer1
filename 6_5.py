"""Programa 6_5.py 
Descrição:Alterar programa da listagem 6_21 de forma a poder trabalhar com vários comandos 
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis
fila = []

# Entrada de dados

último = 10
fila = list(range(1,último+1))


# Processamento e saída de dados

while True:
     print("\nExistem %d clientes na fila" % len(fila))
     print("Fila atual:", fila)
     print("Digite F para adicionar um cliente ao fim da fila,")
     print("ou A para realizar o atendimento. S para sair.")

     operação = input("Operação (F, A ou S):")
     x=0
     sair = False

     while x < len(operação):
          if operação[x] == "A":
               if(len(fila))>0:
                    atendido = fila.pop(0)
                    print("Cliente %d atendido" % atendido)
               else:
                    print("Fila vazia! Ninguém para atender.")
          elif operação[x] == "F":
               último += 1 # Adiciona 0 ticket do novo cliente
               fila.append(último)
          elif operação[x] == "S":
               sair = True
               break
          else:
               print("Operação inválida! %s na posição %d! Digite F, A ou S!" (operação[x]))
          x = x+1
     if(sair):
         break
