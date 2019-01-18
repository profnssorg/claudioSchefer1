"""Programa 6_6.py 
Descrição:Alterar programa da listagem 6_21 de forma a poder trabalhar com duas filas
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis

último = int(0)
fila1 = []
fila2 = []

# Entrada de dados

último = 0
fila1 = []
fila2 = []


# Processamento e saída de dados

while True:
     print("\nExistem %d clientes na fila 1 e %d na fila 2." % (len(fila1), len(fila2)))
     print("Fila 1 atual:", fila1)
     print("Fila 2 autal:", fila2)
     print("Digite F para adicionar um cliente ao fim da fila 1 ou G para fila 2,")
     print("ou A para realizar o atendimento a fila 1 ou B para fila 2")
     print("S para sair.")

     operação = input("Operação (F, G, A, B ou S):")

     x=0
     sair = False
     while x < len(operação):

         if operação[x] == "A" or operação[x] == "F":
            fila = fila1
         else:
            fila = fila2
         if operação[x] == "A" or operação[x]=="B":
             if(len(fila))>0:
                   atendido = fila.pop(0)
                   print("Cliente %d atendido" % atendido)
             else:
                   print("Fila vazia! Ninguém para atender.")

         elif operação[x] == "F" or operação[x]=="G":
             último += 1 
             fila.append(último)
         elif operação[x] == "S":
             sair = True
             break
         else:
             print("Operação inválida: %s na posição %d! Digite apenas F, A ou S!" % (operação[x],x))
         x = x + 1
     if(sair):
        break
