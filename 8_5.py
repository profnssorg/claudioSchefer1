"""Programa 8_5.py 
Descrição: Reescrever a função da listagem 8.5 de forma a utilizar os métodos de pesquisa em lista vistos no cap 7.
Autor:Cláudio Schefer
Data: 
Versão: 001
"""

# Declaração de variáveis

L = []
valor = int (0)

# Entrada de dados

L = [10, 20, 25, 30]


# Processamento

def pesquise (lista, valor):
	if valor in lista:
		return lista.index(valor)
	return None


# Saída de dados

print(pesquise(L, 25))
print(pesquise(L, 27))
