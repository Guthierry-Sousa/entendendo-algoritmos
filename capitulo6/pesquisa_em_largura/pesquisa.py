from fila import Fila

# Pesquisa em largura
def pesquisa_largura(fila: Fila, objeto: str, grafo: dict, start_node: str):

    if start_node == objeto:
        print(f'{start_node} foi encontrado(a)!')
        return True
    
    pais = {}
    
    verificados = set()
    verificados.add(start_node)

    vizinhos_iniciais = grafo.get(start_node, [])

    for vizinho in vizinhos_iniciais:
        fila.enqueue(vizinho)
        pais[vizinho] = start_node

    while not fila.is_empty():
        item = fila.dequeue()

        if item in verificados:
            continue

        if item == objeto:

            print(f'{item} foi encontrado(a)!')

            caminho = []
            atual = objeto

            while not atual is None:

                caminho.append(atual)
                atual = pais.get(atual)

            return caminho[::-1]
                
        else:
            vizinhos = grafo.get(item, [])
            for vizinho in vizinhos:
                if vizinho not in verificados and vizinho not in pais:
                    fila.enqueue(vizinho)
                    pais[vizinho] = item

            verificados.add(item)

    print(f'{objeto} não faz parte do grafo!')
    return None     

objeto = 'jonny'

grafo = {}
grafo['guthy'] = ['alice', 'bob', 'claire']
grafo['bob'] = ['anuj', 'peggy']
grafo['alice'] = ['peggy']
grafo['claire'] = ['thom', 'jonny']
grafo['anuj'] = []
grafo['thom'] = []
grafo['jonny'] = []
grafo['peggy'] = []

queue = Fila() # Instânciando fila

start_node = 'guthy'                   
caminho = pesquisa_largura(fila=queue, objeto=objeto, grafo=grafo, start_node=start_node)
print(f"Caminho Mínimo de '{start_node}' até '{objeto}': {caminho} ")
