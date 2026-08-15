def pesquisa_simples(lista: list, elemento: int) -> int:

    for i in range(len(lista)):

        if lista[i] == elemento:

            return i
            
    return None


lista = [i+1 for i in range(100)]
elemento1 = 88
elemento2 = 130

idx1 = pesquisa_simples(lista=lista, elemento=elemento1)
print(idx1)
idx2 = pesquisa_simples(lista=lista, elemento=elemento2)
print(idx2)

print(lista[idx1] == elemento1)