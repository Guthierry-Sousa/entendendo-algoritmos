def quicksort(lista: list) -> list:

    if len(lista) < 2:

        return lista
    
    pivo = lista[0]

    arr_lower = [i for i in lista[1:] if i <= pivo]
    arr_upper = [i for i in lista[1:] if i > pivo]

    return quicksort(arr_lower) + [pivo] + quicksort(arr_upper)

lista = [33, 10, 15, 7, 33, 33]

print(quicksort(lista))