def pesquisa_binaria_recursiva(lista: list, elemento: int) -> int:

    if not lista:

        return None

    chute = (len(lista) - 1) // 2

    if elemento == lista[chute]:

        return chute
    
    elif elemento < lista[chute]:

        return pesquisa_binaria_recursiva(lista[:chute], elemento)
    
    else:

        resultado_sublista = pesquisa_binaria_recursiva(lista[chute+1:], elemento)
        
        if resultado_sublista is None:
            return None
        else:
            return chute + 1 + resultado_sublista
        

a = int(input("Informe o início do intervalo: "))
b = int(input("Informe o fim do intervalo: "))

lista = [i for i in range(a, b)]
elemento = int(input("Informe o elemento que deseja encontrar o índice: "))

result = pesquisa_binaria_recursiva(lista=lista, elemento=elemento)

if result:

    print(f"{elemento} encontrado no índice: {result}")

else:

    print(f"{elemento} não faz parte da lista!")
    
    
    


