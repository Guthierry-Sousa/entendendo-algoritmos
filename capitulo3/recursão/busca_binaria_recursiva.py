def pesquisa_binaria_recursiva(lista: list, elemento: int, baixo: int = 0, alto: int = None) -> int:

    if alto is None:

        alto = len(lista) - 1

    if (baixo > alto): # Caso-base 1

        return None
    
    chute = (baixo + alto)//2
    
    if lista[chute] == elemento: # Caso-base 2

        return chute
    
    elif elemento > lista[chute]:

        return pesquisa_binaria_recursiva(lista, elemento, baixo = chute+1, alto=alto)

    else:

        return pesquisa_binaria_recursiva(lista, elemento, baixo=baixo, alto=chute - 1)

a = int(input("Informe o início do intervalo: "))
b = int(input("Informe o fim do intervalo: "))

lista = [i for i in range(a, b)]
elemento = int(input("Informe o elemento que deseja encontrar o índice: "))

result = pesquisa_binaria_recursiva(lista=lista, elemento=elemento)

if result:

    print(f"{elemento} encontrado no índice: {result}")

else:

    print(f"{elemento} não faz parte da lista!")