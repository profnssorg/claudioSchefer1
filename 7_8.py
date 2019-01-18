"""Programa 7_8.py 
Descrição: Modificar o programa da listagem 7.45 de modo a escrever a palavra secreta caso o jogador perca.
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis

palavra = ""
digitadas = ""


# Entrada de dados

palavra = input("Digite a palavra secreta:").lower().strip()


# Processamento


palavras = [
          "casa",
          "bola",
          "mangueira",
          "uva"
     ]

índice = int(input("Digite um numero:"))
palavra = palavras[ (índice * 776) % len(palavras)]
for x in range(100):
     print()
digitadas = []
acertos = []
erros = 0
while True:
     senha = ""
     for letra in palavra:
         senha += letra if letra in acertos else "."
     print(senha)
     if senha == palavra:
         print("Você acertou!")
         break
     tentativa = input("\nDigite uma letra:").lower().strip()
     if tentativa in digitadas:
         print("Você já tentou esta letra!")
         continue
     else:
         digitadas += tentativa
         if tentativa in palavra:
               acertos += tentativa
         else:
               erros += 1
               print("Você errou!")
     print("X==:==\nX  :   ")
     print("X  O   " if erros >= 1 else "X")
     linha2 = ""
     if erros == 2:
         linha2 = "  |   "
     elif erros == 3:
         linha2 = " \|   "
     elif erros >= 4:
         linha2 = " \|/ "
     print("X%s" % linha2)
     linha3 = ""
     if erros == 5:
         linha3 += " /     "
     elif erros >= 6:
         linha3 += " / \ "
     print("X%s" % linha3)
     print("X\n===========")
     if erros == 6:


# Saída de dados

         print("Enforcado!")
         print("A palavra secreta era: %s" % palavra)
         break
