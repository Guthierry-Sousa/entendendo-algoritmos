# Escreva o código para somar elementos de um array (recursivamente e iterativamente)

def soma_iterativa(lista: list):

    sum = 0

    for num in lista:

        sum += num

    return sum

def soma_recursiva(lista: list):

    if len(lista) == 1:

        return lista[0]

    else:

        return lista[0] + soma_recursiva(lista[1:]) 
    

lista_teste1 = [1, 3, 10, 1, -10, 4, -5]
lista_teste2 = [9.5, 10, -11.3, 0.45]
print(f"Lista 1: {lista_teste1}")
print(f"Lista 2: {lista_teste2}")

# Teste soma_iterativa:
result = soma_iterativa(lista_teste1)
print(f"Resultado (soma_iterativa): {result}")
result = soma_iterativa(lista_teste2)
print(f"Resultado (soma_iterativa): {result:.2f}")

# Teste soma_recursiva
result = soma_recursiva(lista_teste1)
print(f"Resultado (soma_recursiva): {result}")
result = soma_recursiva(lista_teste2)
print(f"Resultado (soma_recursiva): {result:.2f}")

