def pesquisa_binaria(lista: list, elemento: int) -> int:

    tam_lista = len(lista)

    baixo = 0 # Primeiro elemento da lista

    alto = tam_lista - 1 # Último elemento da lista

    while(baixo <= alto):

        chute = (baixo + alto) // 2 # meio da lista

        if lista[chute] == elemento:

            return chute
            
        elif elemento > lista[chute]:

            baixo = chute + 1

        else:

            alto = chute - 1

    return None


a = int(input("Informe o início do intervalo: "))
b = int(input("Informe o fim do intervalo: "))

lista = [i for i in range(a, b)]
elemento = int(input("Informe o elemento que deseja encontrar o índice: "))

result = pesquisa_binaria(lista=lista, elemento=elemento)

if result:

    print(f"{elemento} encontrado no índice: {result}")

else:

    print(f"{elemento} não faz parte da lista!")

