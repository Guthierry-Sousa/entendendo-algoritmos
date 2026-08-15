def encontrar_vertice_com_menor_peso(pesos: dict, visitados: set):

    menor_peso = float('inf')
    no = None

    for n in pesos.keys():

        if (pesos.get(n) < menor_peso) and (n not in visitados):

            menor_peso = pesos.get(n)
            no = n

    return no

def executar_dijkstra(grafo: dict, pesos: dict, no_final):

    visitados = set()
    pais = dict()

    vertice = encontrar_vertice_com_menor_peso(pesos, visitados)

    while vertice:

        if vertice == no_final:
        
            print(f'{vertice} foi encontrado(a)!')
        
            caminho = []
            atual = no_final
        
            while not atual is None:
        
                caminho.append(atual)
                atual = pais.get(atual)
        
            return caminho[::-1]

        peso = pesos.get(vertice)
        vizinhos = grafo.get(vertice, {})

        for v in vizinhos.keys():

            novo_peso = peso + vizinhos.get(v)

            if novo_peso < pesos.get(v):

                pesos[v] = novo_peso

                pais[v] = vertice

        visitados.add(vertice)
        vertice = encontrar_vertice_com_menor_peso(pesos, visitados)

    return None

pesos = {}

pesos['A'] = 0
pesos['B'] = float('inf')
pesos['C'] = float('inf')
pesos['D'] = float('inf')
pesos['E'] = float('inf')
pesos['F'] = float('inf')

grafo = {}
grafo['A'] = {}
grafo['A']['B'] = 0
grafo['A']['C'] = 5

grafo['B'] = {}
grafo['B']['D'] = 35
grafo['B']['E'] = 30

grafo['C'] = {}
grafo['C']['D'] = 20
grafo['C']['E'] = 15

grafo['D'] = {}
grafo['D']['F'] = 10

grafo['E'] = {}
grafo['E']['F'] = 20

grafo['F'] = {}

caminho = executar_dijkstra(grafo, pesos, 'F')
print(f"Caminho mais curto: {caminho}")

print(f'Custo total: {pesos.get('F')}')