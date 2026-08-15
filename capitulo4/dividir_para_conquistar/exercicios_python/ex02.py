# Escreva uma função recursiva que conte o número de itens em uma lista.

def len_lista(lista: list) -> int:

    if not lista:

        return 0
    
    else:

        return 1 + len_lista(lista=lista[1:])
    
lista_teste = [10, 20, 30, 40, 50]
print(len_lista(lista=lista_teste))

lista_teste = ["Guthy", "Elis", "Elen", 1, 10, 9.3]
print(len_lista(lista=lista_teste))