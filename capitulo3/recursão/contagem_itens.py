def contagem_itens_lista(lista: list) -> int:

    if lista:

        return 1 + contagem_itens_lista(lista[1:])
    
    else:

        return 0
    
lista_teste = [10, 20, 30, 40, 50]
print(contagem_itens_lista(lista=lista_teste))

lista_teste = [1, 2, 10, 4, 5, 65, 3, 2]
print(contagem_itens_lista(lista=lista_teste))

lista_teste = []
print(contagem_itens_lista(lista=lista_teste))
