import time

cache_paginas = {}

def carregar_pagina_do_servidor(url: str) -> str:
    time.sleep(2)
    return f"Conteúdo HTML da página: {url}"

def carregar_pagina(url: str):

    if cache_paginas.get(url):

        print("Página Carregada (Instantaneamente)!")

        return cache_paginas[url]
    
    print("Carregando página...")
    
    conteudo = carregar_pagina_do_servidor(url)

    cache_paginas[url] = conteudo

    return conteudo

print("--- Primeira Chamada ---")
inicio = time.time()
print(carregar_pagina("meusite.com/python"))
print(f"Tempo decorrido: {time.time() - inicio:.2f} segundos\n")

print("--- Segunda Chamada ---")
inicio = time.time()
print(carregar_pagina("meusite.com/python"))
print(f"Tempo decorrido: {time.time() - inicio:.2f} segundos\n")