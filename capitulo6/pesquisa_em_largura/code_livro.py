# Implementação do livro 

from collections import deque

grafo = {}
grafo['guthy'] = ['alice', 'bob', 'claire']
grafo['bob'] = ['anuj', 'peggy']
grafo['alice'] = ['peggy']
grafo['claire'] = ['thom', 'jonny']
grafo['anuj'] = []
grafo['thom'] = []
grafo['jonny'] = []
grafo['peggy'] = []

def pesquisa(no_inicial, destino):

    if no_inicial == destino:
        return True

    fila = deque()
    fila += grafo[no_inicial]
    verificadas = set()

    verificadas.add(no_inicial)

    while fila:

        no = fila.popleft()

        if no not in verificadas:

            if no == destino:
                print(f'{destino} encontrado(a)!')
                return True
            
            else:

                fila += grafo[no]
                verificadas.add(no)
    print(f'{destino} não encontrado(a)!')
    return False

pesquisa('guthy', 'anuj')
pesquisa('guthy', 'elis')