def list_invert(array: list) -> list:

    n = len(array) - 1
    new_arr = []

    for i in range(n, -1, -1):

        new_arr.append(array[i])

    return new_arr

def list_invert2(array: list) -> list:

    n = len(array) 

    for i in range(n//2):

        aux = array[i]
        array[i] = array[(n - i) - 1]
        array[(n - i) - 1] = aux

    return array

def list_invert3(array: list) -> list:

    n = len(array)

    for i, j in zip(range(0, n//2),range(n-1, (n//2) - 1, -1)):

        aux = array[i]
        array[i] = array[j]
        array[j] = aux

    return array

def list_invert4(array: list) -> list:

    start = 0
    end = len(array) - 1

    while start < end:

        aux = array[start]
        array[start] = array[end]
        array[end] = aux

        start += 1 
        end -= 1

    return array

lista = [1, 2, 3, 4]
print(list_invert4(lista))