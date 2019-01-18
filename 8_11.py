"""Programa 8_11.py 
Descrição: Escrever uma função para validar uma variável string.
A função recebe como parâmetro a string, o número mínimo e máximo de caracteres.
Retornar verdadeiro se a string estiver entre os valores máximo e mínimo, e falso em caso contrário.
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis

s = ""


# Entrada de dados

s = input("Digite a string: ")

# Processamento

def valida_string(s,mín,máx):
    tamanho = len(s)

    if mín <= tamanho <= máx:
        return True
    else:
        return False

# Saída de dados

print (valida_string ("s", 1,8))
