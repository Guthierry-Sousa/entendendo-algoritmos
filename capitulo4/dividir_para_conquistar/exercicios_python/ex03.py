# Escreva uma função recursiva que encontre o maior valor de uma lista.

def max_value(lista: list, maior = None):

    if not lista:

        return maior

    if maior is None:

            maior = lista[0]

    else:

        maior = max(lista[0], maior)


    return max_value(lista=lista[1:], maior=maior)

def max_value_dc(lista: list):

    if not lista:
         
        return None

    if len(lista) == 1:
         
        return lista[0]
    
    else:

        maior = lista[0]
         
        return max(maior, max_value_dc(lista=lista[1:]))

lista_teste = [1]

print(max_value_dc(lista_teste))
    
