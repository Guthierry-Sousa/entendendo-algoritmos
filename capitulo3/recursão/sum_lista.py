def somar_elementos(lista: list):

    if len(lista) == 0:

        return 0
    
    else:

        elemento = lista[0]
        lista_restante = lista[1:]

        return elemento + somar_elementos(lista_restante)
    
def somar_elementos_pop(lista: list[int]) -> int:

    if len(lista) == 0:

        return 0
    
    else:

        elemento = lista.pop()

        return elemento + somar_elementos(lista)
    
    

print(somar_elementos_pop([2, 4, 6, 8]))